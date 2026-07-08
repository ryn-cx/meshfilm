# TODO: Validate
"""Title API endpoint."""

from __future__ import annotations

from typing import Any

from meshfilm._graphql import group_by_type
from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.title.models import Title as TitleModel


class Title(BaseEndpoint[TitleModel]):
    """Provides methods to download, parse, and retrieve Netflix title data."""

    _response_model = TitleModel

    BASE_URL = "https://www.netflix.com/title/"

    @classmethod
    def clean_data(cls, data: dict[str, Any]) -> dict[str, Any]:
        """Group the raw cache's mixed type+id keys into per-type lists.

        The download is saved exactly as received; this reshaping happens on the
        way into ``parse()`` and model generation only.
        """
        return group_by_type(data)

    def download(self, title_id: str) -> dict[str, Any]:
        """Downloads the GraphQL cache for a given Netflix title ID.

        Args:
            title_id: The numeric Netflix title ID (e.g. ``"80240027"``).

        Returns:
            The raw grouped GraphQL cache, suitable for passing to ``parse()``.
        """
        url = f"{self.BASE_URL}{title_id}"
        return self._client.download(url)

    def get(self, title_id: str) -> TitleModel:
        """Downloads and parses the data for a given Netflix title ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            title_id: The numeric Netflix title ID (e.g. ``"80240027"``).

        Returns:
            A Title model containing the parsed data.
        """
        data = self.download(title_id)
        return self.parse(data)
