# TODO: Validate
"""Contains the PreviewModalEpisodeSelectorSeasonEpisodes class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.preview_modal_episode_selector_season_episodes.models import (
    PreviewModalEpisodeSelectorSeasonEpisodesModel,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

DEFAULT_EPISODE_COUNT = 30


class PreviewModalEpisodeSelectorSeasonEpisodes(
    BaseEndpoint[PreviewModalEpisodeSelectorSeasonEpisodesModel],
):
    """Manage the preview modal episode selector season episodes file."""

    _response_model = PreviewModalEpisodeSelectorSeasonEpisodesModel

    def get_log_id(
        self,
        season_id: str | int,
        count: int = DEFAULT_EPISODE_COUNT,
    ) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {season_id=}",
            count=(count, DEFAULT_EPISODE_COUNT),
        )

    def _payload(self, season_id: str | int, count: int) -> dict[str, Any]:
        return {
            "operationName": "PreviewModalEpisodeSelectorSeasonEpisodes",
            "variables": {
                "seasonId": int(season_id),
                "count": count,
                "opaqueImageFormat": "JPG",
                "artworkContext": {},
            },
            "extensions": {
                "persistedQuery": {
                    "id": "27b30e4e-871d-46aa-ac8b-244103d2e37d",
                    "version": 102,
                },
            },
        }

    def download(
        self,
        season_id: str | int,
        count: int = DEFAULT_EPISODE_COUNT,
    ) -> dict[str, Any]:
        """Downloads the preview modal episode selector season episodes file."""
        return self._client.download(
            self._payload(season_id, count),
            log_id=self.get_log_id(season_id, count),
        )

    def download_and_parse(
        self,
        season_id: str | int,
        count: int = DEFAULT_EPISODE_COUNT,
    ) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
        """Downloads and parses the preview modal episode selector season episodes."""
        return self.parse(self.download(season_id, count))
