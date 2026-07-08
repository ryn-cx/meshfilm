# TODO: Validate
"""meshfilm is a client for downloading and parsing public Netflix data."""

from __future__ import annotations

import gzip
import http.client
import zlib
from datetime import datetime
from logging import NullHandler, getLogger
from typing import Any
from urllib.error import HTTPError as UrllibHTTPError
from urllib.request import Request, urlopen

from meshfilm._graphql import extract_graphql
from meshfilm.exceptions import HTTPError
from meshfilm.title import Title

DEFAULT_TIMEOUT = 30

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class MeshFilm:
    """Interface for downloading and parsing public Netflix title data."""

    # A browser-like UA is needed or Netflix returns a stripped/redirect page.
    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    )

    def __init__(self, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize the meshfilm client."""
        self.timeout = timeout
        self.title = Title(self)

    def _fetch_html(self, url: str) -> str:
        """Fetch a page's HTML, handling gzip/deflate and partial reads.

        gzip is requested because the plain (identity) response tends to drop the
        connection mid-stream (``IncompleteRead``) before the GraphQL cache, which
        sits near the end of the page.
        """
        request = Request(  # noqa: S310 - fixed https netflix host
            url,
            headers={
                "User-Agent": self.USER_AGENT,
                "Accept-Language": "en-US,en;q=0.9",
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Encoding": "gzip, deflate",
            },
        )
        logger.info("Downloading page: %s", url)
        try:
            with urlopen(request, timeout=self.timeout) as response:  # noqa: S310
                try:
                    raw = response.read()
                except http.client.IncompleteRead as error:
                    raw = error.partial  # salvage what arrived
                encoding = (response.headers.get("Content-Encoding") or "").lower()
                charset = response.headers.get_content_charset() or "utf-8"
        except UrllibHTTPError as error:
            msg = f"Unexpected response status code: {error.code}"
            raise HTTPError(msg) from error

        if encoding == "gzip":
            raw = gzip.decompress(raw)
        elif encoding == "deflate":
            raw = zlib.decompress(raw)
        return raw.decode(charset, errors="replace")

    def download(self, url: str) -> dict[str, Any]:
        """Download a Netflix page and return its raw embedded GraphQL cache.

        The returned dict is the Apollo cache exactly as extracted from the page
        (``{"data": {...}}``) plus a ``meshfilm`` key recording the request.

        Args:
            url: The full URL of the Netflix page to download.

        Returns:
            The raw GraphQL cache, suitable for passing to ``parse()``.
        """
        html = self._fetch_html(url)
        output = extract_graphql(html)
        output["meshfilm"] = {
            "url": url,
            "timestamp": (
                datetime.now().astimezone().isoformat().replace("+00:00", "Z")
            ),
        }
        return output
