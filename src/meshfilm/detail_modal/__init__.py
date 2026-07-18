# TODO: Validate
"""Contains the DetailModal class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.detail_modal.models import DetailModalModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class DetailModal(BaseEndpoint[DetailModalModel]):
    """Manage the detail modal file."""

    _response_model = DetailModalModel

    def get_log_id(self, video_id: str | int) -> str:
        """Build the log id for a download."""
        return f"{self.__class__.__name__} {video_id=}"

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
            log_id=self.get_log_id(video_id),
        )

    def download_and_parse(self, video_id: str | int) -> DetailModalModel:
        """Downloads and parses the detail modal file."""
        return self.parse(self.download(video_id))
