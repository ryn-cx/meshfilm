# TODO: Validate
"""Contains the LodpTitleAndPlansPage class."""

from __future__ import annotations

from typing import Any, override

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.lodp_title_and_plans_page.models import LodpTitleAndPlansPageModel

# The entity types this page serves; a Season (or unknown ID) is not a title.
_TITLE_TYPENAMES = {"Show", "Movie", "Episode"}


class LodpTitleAndPlansPage(BaseEndpoint[LodpTitleAndPlansPageModel]):
    """Manage the lodp title and plans page file."""

    _response_model = LodpTitleAndPlansPageModel

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
            log_id=f"{self.__class__.__name__} {video_id}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any], video_id: str | int) -> bool:
        videos: list[dict[str, Any] | None] = response["data"]["videos"] or []
        entity = next(
            (v for v in videos if v and v.get("videoId") == int(video_id)),
            None,
        )
        return entity is not None and entity.get("__typename") in _TITLE_TYPENAMES

    def get(self, video_id: str | int) -> LodpTitleAndPlansPageModel:
        """Downloads and parses the lodp title and plans page file.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        response = self.download(video_id)
        return self._parse_or_raise(response, f"{self.__class__.__name__} {video_id}")
