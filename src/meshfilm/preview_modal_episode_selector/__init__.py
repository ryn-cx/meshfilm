# TODO: Validate
"""Contains the PreviewModalEpisodeSelector class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import InvalidFileError
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
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            self._payload(show_id, season_count),
            log_id=log_id,
        )
        videos = data.get("data", {}).get("videos") or [{}]
        if videos[0].get("videoId") != int(show_id):
            raise InvalidFileError(field="show id", expected=int(show_id))
        return data

    def download_and_parse(
        self,
        show_id: str | int,
        season_count: int = DEFAULT_SEASON_COUNT,
    ) -> PreviewModalEpisodeSelectorModel:
        """Downloads and parses the preview modal episode selector file."""
        return self.parse(self.download(show_id, season_count))
