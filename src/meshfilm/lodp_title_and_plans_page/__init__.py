# TODO: Validate
"""Contains the LodpTitleAndPlansPage class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.lodp_title_and_plans_page.models import LodpTitleAndPlansPageModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class LodpTitleAndPlansPage(BaseEndpoint[LodpTitleAndPlansPageModel]):
    """Manage the lodp title and plans page file."""

    _response_model = LodpTitleAndPlansPageModel

    def get_log_id(self, video_id: str | int) -> str:
        """Build the log id for a download."""
        return f"{self.__class__.__name__} {video_id=}"

    def _payload(self, video_id: str | int) -> dict[str, Any]:
        return {
            "operationName": "LodpTitleAndPlansPageQuery",
            "variables": {
                "videoId": int(video_id),
                "opaqueImageFormat": "JPG",
                "transparentImageFormat": "PNG",
                "thumbnailVideoId": -1,
                "hasValidThumbnailVideoId": False,
                "useBakedInPlayThumbnail": False,
                "useFromWatchSupplements": False,
            },
            "extensions": {
                "persistedQuery": {
                    "id": "807ffc59-06c3-45b1-bd84-b9b4136381fc",
                    "version": 102,
                },
            },
        }

    def download(self, video_id: str | int) -> dict[str, Any]:
        """Downloads the lodp title and plans page file."""
        return self._client.download(
            self._payload(video_id),
            log_id=self.get_log_id(video_id),
        )

    def download_and_parse(self, video_id: str | int) -> LodpTitleAndPlansPageModel:
        """Downloads and parses the lodp title and plans page file."""
        return self.parse(self.download(video_id))
