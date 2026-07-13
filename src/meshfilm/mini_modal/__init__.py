# TODO: Validate
"""Contains the MiniModal class."""

from __future__ import annotations

from typing import Any, override

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.mini_modal.models import MiniModalModel


class MiniModal(BaseEndpoint[MiniModalModel]):
    """Manage the mini modal file."""

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
        """Downloads the mini modal file."""
        joined_ids = "/".join(str(video_id) for video_id in video_ids)
        return self._client.download(
            self._payload(video_ids),
            log_id=f"{self.__class__.__name__} {joined_ids}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any], video_ids: list[str | int]) -> bool:
        entities = response["data"]["unifiedEntities"]
        found_ids = {entity["videoId"] for entity in entities}
        return any(int(video_id) in found_ids for video_id in video_ids)

    def get(self, video_ids: list[str | int]) -> MiniModalModel:
        """Downloads and parses the mini modal file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        joined_ids = "/".join(str(video_id) for video_id in video_ids)
        response = self.download(video_ids)
        return self._parse_or_raise(
            response,
            f"{self.__class__.__name__} {joined_ids}",
            video_ids,
        )
