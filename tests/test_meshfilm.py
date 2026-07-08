# TODO: Validate
"""Test for meshfilm."""

from __future__ import annotations

import json

import pytest

from meshfilm import MeshFilm
from meshfilm.exceptions import GraphQLNotFoundError, HTTPError

client = MeshFilm()

# Virgin River — a stable public title used as the reference throughout.
VIRGIN_RIVER_ID = "80240027"


class TestGet:
    """Test live get requests across every endpoint."""

    def test_get_title(self) -> None:
        """Test getting a title."""
        model = client.title.get(VIRGIN_RIVER_ID)
        raw = client.title.dump(model)
        client.title.save_new_json_file(raw)
        # The saved/dumped data is exactly the raw download (mixed type+id keys).
        assert f'Show:{{"videoId":{VIRGIN_RIVER_ID}}}' in raw["data"]
        # But modify_data groups it, so the parsed model exposes per-type lists.
        assert any(show.title == "Virgin River" for show in model.shows)


class TestInvalidGet:
    """Test get requests for missing or invalid resources."""

    def test_invalid_get_title(self) -> None:
        """Test getting an invalid title.

        Netflix serves a challenge/redirect page (no GraphQL cache) or a 404 for
        an unknown title ID, so either error is acceptable.
        """
        with pytest.raises((HTTPError, GraphQLNotFoundError)):
            client.title.get("0000000")


class TestParse:
    """Test parsing every saved file for each endpoint."""

    def test_parse_title(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.title.json_files():
            client.title.parse(json.loads(json_file.read_text()))
