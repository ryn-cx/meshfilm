# TODO: Validate
r"""Extract the GraphQL cache embedded in a Netflix title page.

A public Netflix title page ships a pre-warmed Apollo cache in:

    netflix.reactContext.models.graphql = JSON.parse('{ ...JS string literal... }');

The argument is a *JS* string literal (with ``\xHH`` escapes that JSON can't
parse), so it is decoded in two steps: unescape the JS literal, then ``json.loads``
the result.
"""

from __future__ import annotations

import codecs
import json
from typing import Any

from meshfilm.exceptions import GraphQLNotFoundError

MARKER = "netflix.reactContext.models.graphql = JSON.parse('"


def decode_js_string(body: str) -> str:
    r"""Decode a JavaScript single-quoted string literal body to its value.

    Handles ``\\`` ``\'`` ``\"`` ``\/`` ``\n`` ``\t`` ``\r`` ``\xHH`` ``\uHHHH``
    etc. Python's ``unicode_escape`` understands all of these except the
    JS-specific ``\'`` and ``\/``, which are normalized first.
    """
    body = body.replace("\\'", "'").replace("\\/", "/")
    return codecs.decode(body.encode("latin-1", "backslashreplace"), "unicode_escape")


def extract_graphql(html: str) -> dict[str, Any]:
    """Extract and decode the embedded Apollo cache from a page's HTML.

    Args:
        html: The full HTML of a Netflix title page.

    Returns:
        The decoded GraphQL cache, i.e. ``{"data": {<key>: <entity>, ...}}``.

    Raises:
        GraphQLNotFoundError: If the page has no embedded GraphQL cache.
    """
    start = html.find(MARKER)
    if start == -1:
        msg = "No embedded GraphQL cache found on the page."
        raise GraphQLNotFoundError(msg)
    body_start = start + len(MARKER)
    # The literal's only unescaped single quote is its terminator, immediately
    # followed by ")". So "');" marks the end of the argument.
    end = html.find("');", body_start)
    if end == -1:
        msg = "Could not find the end of the GraphQL literal."
        raise GraphQLNotFoundError(msg)
    return json.loads(decode_js_string(html[body_start:end]))


def _pluralize(name: str) -> str:
    """Pluralize a type-name stem (movie -> movies, query -> queries)."""
    if name.endswith("y") and name[-2:-1].lower() not in "aeiou":
        return name[:-1] + "ies"
    return name + "s"


def _slug(value: str) -> str:
    """Lowercase an enum-ish string into a field-name-safe fragment."""
    return "".join(c if c.isalnum() else "_" for c in value).strip("_").lower()


def _scalar_leaves(obj: Any) -> list[str]:  # noqa: ANN401
    """Collect discriminating scalar args (strings and numbers) in order.

    Booleans are skipped: flags like ``nonMemberBranding: true`` are noise that
    never distinguish one variant from another.
    """
    if isinstance(obj, dict):
        return [leaf for v in obj.values() for leaf in _scalar_leaves(v)]
    if isinstance(obj, list):
        return [leaf for v in obj for leaf in _scalar_leaves(v)]
    if isinstance(obj, bool):
        return []
    if isinstance(obj, str):
        return [obj]
    if isinstance(obj, (int, float)):
        return [str(obj)]
    return []


def _clean_field_key(key: str) -> str:
    r"""Flatten an Apollo storeFieldName (field + serialized args) to a short name.

    Apollo bakes a field's arguments into its storage key, e.g.
    ``artwork({"params":{"artworkType":"BILLBOARD",...}})`` or
    ``persons:{"roles":"ACTOR"}``. This reduces such a key to its base name plus
    the discriminating scalar args::

        artwork({"params":{"artworkType":"BILLBOARD",...,"format":"JPG"}})
            -> artwork_billboard_1280_story_art_jpg
        persons:{"roles":"ACTOR"}   -> persons_actor

    Non-argument keys (``title``, ``videoId``, ``__typename``, ...) are returned
    unchanged.
    """
    for sep in ("(", ":"):
        idx = key.find(sep)
        # An argument blob always opens with "{" or "[" right after the separator.
        if idx <= 0 or key[idx + 1 : idx + 2] not in ("{", "["):
            continue
        base = key[:idx]
        blob = key[idx + 1 :]
        if sep == "(" and blob.endswith(")"):
            blob = blob[:-1]
        try:
            args = json.loads(blob)
        except ValueError:
            return key
        values = [_slug(v) for v in _scalar_leaves(args)]
        return "_".join([base, *values]) if values else base
    return key


def _normalize_keys(obj: Any) -> Any:  # noqa: ANN401
    """Recursively rewrite Apollo storeFieldName keys to clean field names.

    Collisions (two argument variants that reduce to the same name) are
    disambiguated with a numeric suffix so no field is ever dropped.
    """
    if isinstance(obj, dict):
        out: dict[str, Any] = {}
        for key, value in obj.items():
            clean = _clean_field_key(key)
            if clean in out:
                suffix = 2
                while f"{clean}_{suffix}" in out:
                    suffix += 1
                clean = f"{clean}_{suffix}"
            out[clean] = _normalize_keys(value)
        return out
    if isinstance(obj, list):
        return [_normalize_keys(v) for v in obj]
    return obj


def group_by_type(data: dict[str, Any]) -> dict[str, Any]:
    r"""Group the flat Apollo cache into per-type lists.

    The raw cache mixes each entity's type and id into one key
    (``{"Show:{\"videoId\":80240027}": {...}, "Movie:{...}": {...}}``). This
    turns it into ``{"shows": [...], "movies": [...], ...}``. ``ROOT_QUERY``
    (``__typename`` "Query") is navigation scaffolding and is dropped. Any
    sibling metadata (e.g. the ``meshfilm`` key) is passed through.
    """
    groups: dict[str, Any] = {}
    for node in data["data"].values():
        if not isinstance(node, dict):
            continue
        typename = node.get("__typename", "Unknown")
        if typename == "Query":
            continue
        bucket = _pluralize(typename[0].lower() + typename[1:])
        groups.setdefault(bucket, []).append(_normalize_keys(node))
    groups.update({key: value for key, value in data.items() if key != "data"})
    return groups
