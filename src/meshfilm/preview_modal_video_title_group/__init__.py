# TODO: Validate
from __future__ import annotations

from typing import Any, override

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
        return self._client.download(self._payload(video_ids), video_ids)

    @staticmethod
    @override
    def has_content(response: dict[str, Any], video_ids: list[str | int]) -> bool:
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

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        response = self.download(video_ids)
        return self._parse_or_raise(
            response,
            has_content=self.has_content(response, video_ids),
        )
