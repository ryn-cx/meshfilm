from __future__ import annotations

from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.detail_modal.models import DetailModalModel


class DetailModal(BaseEndpoint[DetailModalModel]):
    """A video's detail-modal data and its playback availability."""

    _response_model = DetailModalModel

    def _payload(self, video_id: str | int) -> dict[str, Any]:
        return {
            "operationName": "DetailModal",
            "variables": {
                "opaqueImageFormat": "JPG",
                "transparentImageFormat": "PNG",
                "videoMerchEnabled": False,
                "fetchPromoVideoOverride": False,
                "hasPromoVideoOverride": True,
                "promoVideoId": 0,
                "videoMerchContext": "BROWSE",
                "isLiveEpisodic": False,
                "artworkContext": {},
                "textEvidenceUiContext": "ODP",
                "unifiedEntityId": f"Video:{video_id}",
                "videoId": int(video_id),
                "checkLinearChannel": True,
            },
            "extensions": {
                "persistedQuery": {
                    "id": "8bb4b13e-a6d6-455a-b821-7ae7804577a4",
                    "version": 102,
                },
            },
        }

    def download(self, video_id: str | int) -> dict[str, Any]:
        """Downloads the DetailModal for a given Netflix video ID.

        Args:
            video_id: The numeric Netflix video ID of an Episode, also accepts a Show,
            Movie, or Season.

        Returns:
            The raw GraphQL response, suitable for passing to `parse()`.
        """
        return self._client.download(self._payload(video_id), video_id)

    @staticmethod
    def has_content(response: dict[str, Any]) -> bool:
        """Return whether the response has meaningful content."""
        return bool(response["data"]["unifiedEntities"])

    def get(self, video_id: str | int) -> DetailModalModel:
        """Downloads and parses the DetailModal for a given Netflix video ID.

        Args:
            video_id: The numeric Netflix video ID of an Episode, also accepts a Show,
            Movie, or Season.

        Returns:
            A DetailModal model containing the parsed data.
        """
        return self.parse(self.download(video_id))
