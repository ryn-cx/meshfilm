# TODO: Validate
"""Contains the PreviewModalEpisodeSelector class."""

from __future__ import annotations

from typing import Any, override

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.preview_modal_episode_selector.models import (
    PreviewModalEpisodeSelectorModel,
)

DEFAULT_SEASON_COUNT = 5


class PreviewModalEpisodeSelector(
    BaseEndpoint[PreviewModalEpisodeSelectorModel],
):
    """Manage the preview modal episode selector file."""

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
        """Downloads the preview modal episode selector file."""
        return self._client.download(
            self._payload(show_id, season_count),
            log_id=f"{self.__class__.__name__} {show_id}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any], show_id: str | int) -> bool:
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
        """Downloads and parses the preview modal episode selector file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        response = self.download(show_id, season_count)
        return self._parse_or_raise(
            response,
            f"{self.__class__.__name__} {show_id}",
            show_id,
        )
