# TODO: Validate
"""Contains the DetailModal class."""

from __future__ import annotations

from typing import Any, override

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.detail_modal.models import DetailModalModel


class DetailModal(BaseEndpoint[DetailModalModel]):
    """Manage the detail modal file."""

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
        """Downloads the detail modal file."""
        return self._client.download(
            self._payload(video_id),
            log_id=f"{self.__class__.__name__} {video_id}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response["data"]["unifiedEntities"])

    def get(self, video_id: str | int) -> DetailModalModel:
        """Downloads and parses the detail modal file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        response = self.download(video_id)
        return self._parse_or_raise(response, f"{self.__class__.__name__} {video_id}")
