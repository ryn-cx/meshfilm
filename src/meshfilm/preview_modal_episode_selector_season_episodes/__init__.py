# TODO: Validate
from __future__ import annotations

from typing import Any, override

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.preview_modal_episode_selector_season_episodes.models import (
    PreviewModalEpisodeSelectorSeasonEpisodesModel,
)

DEFAULT_EPISODE_COUNT = 30


class PreviewModalEpisodeSelectorSeasonEpisodes(
    BaseEndpoint[PreviewModalEpisodeSelectorSeasonEpisodesModel],
):
    """The episodes of a season, with each episode's metadata and artwork."""

    _response_model = PreviewModalEpisodeSelectorSeasonEpisodesModel

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
        """Downloads the episodes for a given Netflix season ID.

        Args:
            season_id: The numeric Netflix video ID of a Season; no other type
            is accepted.
            count: The maximum number of episodes to request

        Returns:
            The raw GraphQL response, suitable for passing to `parse()`.
        """
        return self._client.download(
            self._payload(season_id, count),
            season_id,
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any], season_id: str | int) -> bool:
        videos: list[dict[str, Any] | None] = response["data"]["videos"] or []
        entity = next(
            (v for v in videos if v and v.get("videoId") == int(season_id)),
            None,
        )
        return entity is not None and entity.get("__typename") == "Season"

    def get(
        self,
        season_id: str | int,
    ) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
        """Downloads and parses the episodes for a given Netflix season ID.

        Args:
            season_id: The numeric Netflix video ID of a Season.

        Returns:
            A PreviewModalEpisodeSelectorSeasonEpisodes model with the data.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        response = self.download(season_id)
        return self._parse_or_raise(
            response,
            has_content=self.has_content(response, season_id),
        )
