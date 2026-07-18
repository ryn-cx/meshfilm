# TODO: Validate
"""Contains the PreviewModalEpisodeSelector class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.preview_modal_episode_selector.models import (
    PreviewModalEpisodeSelectorModel,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

DEFAULT_SEASON_COUNT = 5


class PreviewModalEpisodeSelector(
    BaseEndpoint[PreviewModalEpisodeSelectorModel],
):
    """Manage the preview modal episode selector file."""

    _response_model = PreviewModalEpisodeSelectorModel

    def get_log_id(
        self,
        show_id: str | int,
        season_count: int = DEFAULT_SEASON_COUNT,
    ) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {show_id=}",
            season_count=(season_count, DEFAULT_SEASON_COUNT),
        )

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
            log_id=self.get_log_id(show_id, season_count),
        )

    def download_and_parse(
        self,
        show_id: str | int,
        season_count: int = DEFAULT_SEASON_COUNT,
    ) -> PreviewModalEpisodeSelectorModel:
        """Downloads and parses the preview modal episode selector file."""
        return self.parse(self.download(show_id, season_count))
