# TODO: Validate
"""Contains the MiniModal class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.mini_modal.models import MiniModalModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class MiniModal(BaseEndpoint[MiniModalModel]):
    """Manage the mini modal file."""

    _response_model = MiniModalModel

    def get_log_id(self, video_ids: list[str | int]) -> str:
        """Build the log id for a download."""
        return f"{self.__class__.__name__} {video_ids=}"

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
        """Downloads the mini modal file."""
        return self._client.download(
            self._payload(video_ids),
            log_id=self.get_log_id(video_ids),
        )

    def download_and_parse(self, video_ids: list[str | int]) -> MiniModalModel:
        """Downloads and parses the mini modal file."""
        return self.parse(self.download(video_ids))
