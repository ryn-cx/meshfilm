from __future__ import annotations

from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.preview_modal_video_title_group.models import (
    PreviewModalVideoTitleGroupModel,
)


class PreviewModalVideoTitleGroup(BaseEndpoint[PreviewModalVideoTitleGroupModel]):
    """Title-group preview data for a batch of videos."""

    _response_model = PreviewModalVideoTitleGroupModel

    def _payload(self, video_ids: list[str | int]) -> dict[str, Any]:
        return {
            "operationName": "PreviewModalVideoTitleGroup",
            "variables": {
                "artworkContext": {},
                "videoIds": [int(video_id) for video_id in video_ids],
            },
            "extensions": {
                "persistedQuery": {
                    "id": "45e04e0a-46b0-436e-b506-de5c46466fba",
                    "version": 102,
                },
            },
        }

    def download(self, video_ids: list[str | int]) -> dict[str, Any]:
        """Downloads the title-group preview for a batch of Netflix video IDs.

        Args:
            video_ids: The numeric Netflix video IDs of Shows, also accepts
            Movies, Episodes, or Seasons.

        Returns:
            The raw GraphQL response, suitable for passing to `parse()`.
        """
        return self._client.download_graphql(self._payload(video_ids), video_ids)

    @staticmethod
    def has_content(response: dict[str, Any], video_ids: list[str | int]) -> bool:
        """Return whether the response has meaningful content."""
        videos = response["data"]["videos"]
        return any(
            index < len(videos) and videos[index] is not None
            for index in range(len(video_ids))
        )

    def get(self, video_ids: list[str | int]) -> PreviewModalVideoTitleGroupModel:
        """Downloads and parses the title-group preview for a batch of video IDs.

        Args:
            video_ids: The numeric Netflix video IDs of Shows, also accepts
            Movies, Episodes, or Seasons.

        Returns:
            A PreviewModalVideoTitleGroup model containing the parsed data.
        """
        return self.parse(self.download(video_ids))
