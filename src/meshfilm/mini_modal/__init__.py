from __future__ import annotations

from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.mini_modal.models import MiniModalModel


class MiniModal(BaseEndpoint[MiniModalModel]):
    """Hover-preview data for a batch of videos."""

    _response_model = MiniModalModel

    def _payload(self, video_ids: list[str | int]) -> dict[str, Any]:
        return {
            "operationName": "MiniModalQuery",
            "variables": {
                "opaqueImageFormat": "JPG",
                "transparentImageFormat": "PNG",
                "videoMerchEnabled": False,
                "fetchPromoVideoOverride": False,
                "hasPromoVideoOverride": False,
                "promoVideoId": 0,
                "videoMerchContext": "BROWSE",
                "isLiveEpisodic": False,
                "artworkContext": {},
                "textEvidenceUiContext": "BOB",
                "unifiedEntityIds": [f"Video:{video_id}" for video_id in video_ids],
            },
            "extensions": {
                "persistedQuery": {
                    "id": "e52d138c-9808-4fea-a01f-27bfcf9d5041",
                    "version": 102,
                },
            },
        }

    def download(self, video_ids: list[str | int]) -> dict[str, Any]:
        """Downloads the MiniModal for a batch of Netflix video IDs.

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
        entities = response["data"]["unifiedEntities"]
        found_ids = {entity["videoId"] for entity in entities}
        return any(int(video_id) in found_ids for video_id in video_ids)

    def get(self, video_ids: list[str | int]) -> MiniModalModel:
        """Downloads and parses the MiniModal for a batch of Netflix video IDs.

        Args:
            video_ids: The numeric Netflix video IDs of Shows, also accepts
            Movies, Episodes, or Seasons.

        Returns:
            A MiniModal model containing the parsed data.
        """
        return self.parse(self.download(video_ids))
