from __future__ import annotations

from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.preview_modal_episode_selector.models import (
    PreviewModalEpisodeSelectorModel,
)

DEFAULT_SEASON_COUNT = 5


class PreviewModalEpisodeSelector(
    BaseEndpoint[PreviewModalEpisodeSelectorModel],
):
    """The seasons of a show, for the preview-modal episode selector."""

    _response_model = PreviewModalEpisodeSelectorModel

    def _payload(self, show_id: str | int, season_count: int) -> dict[str, Any]:
        return {
            "operationName": "PreviewModalEpisodeSelector",
            "variables": {
                "showId": int(show_id),
                "seasonCount": season_count,
            },
            "extensions": {
                "persistedQuery": {
                    "id": "dbc3b274-d4f9-4811-aaf1-d082d3b936f2",
                    "version": 102,
                },
            },
        }

    def download(
        self,
        show_id: str | int,
        season_count: int = DEFAULT_SEASON_COUNT,
    ) -> dict[str, Any]:
        """Downloads the season selector for a given Netflix show ID.

        Args:
            show_id: The numeric Netflix video ID of a Show; no other type is
            accepted.
            season_count: The maximum number of seasons to request

        Returns:
            The raw GraphQL response, suitable for passing to `parse()`.
        """
        return self._client.download_graphql(
            self._payload(show_id, season_count),
            show_id,
        )

    @staticmethod
    def has_content(response: dict[str, Any], show_id: str | int) -> bool:
        """Return whether the response has meaningful content."""
        videos: list[dict[str, Any] | None] = response["data"]["videos"] or []
        entity = next(
            (v for v in videos if v and v.get("videoId") == int(show_id)),
            None,
        )
        return entity is not None and entity.get("__typename") == "Show"

    def get(
        self,
        show_id: str | int,
        season_count: int = DEFAULT_SEASON_COUNT,
    ) -> PreviewModalEpisodeSelectorModel:
        """Downloads and parses the season selector for a given Netflix show ID.

        Args:
            show_id: The numeric Netflix video ID of a Show; no other type is
            accepted.
            season_count: The maximum number of seasons to request

        Returns:
            A PreviewModalEpisodeSelector model containing the parsed data.
        """
        return self.parse(self.download(show_id, season_count))
