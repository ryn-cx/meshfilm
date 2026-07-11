from __future__ import annotations

from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.lodp_title_and_plans_page.models import LodpTitleAndPlansPageModel

# The entity types this page serves; a Season (or unknown ID) is not a title.
_TITLE_TYPENAMES = {"Show", "Movie", "Episode"}


class LodpTitleAndPlansPage(BaseEndpoint[LodpTitleAndPlansPageModel]):
    """A title's details, related titles, and subscription plans."""

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
        """Downloads the LodpTitleAndPlansPage for a given Netflix video ID.

        Args:
            video_id: The numeric Netflix video ID of a Show, also accepts a
            Movie or Episode.

        Returns:
            The raw GraphQL response, suitable for passing to `parse()`.
        """
        return self._client.download(self._payload(video_id), video_id)

    @staticmethod
    def has_content(response: dict[str, Any], video_id: str | int) -> bool:
        """Return whether the response has meaningful content."""
        videos: list[dict[str, Any] | None] = response["data"]["videos"] or []
        entity = next(
            (v for v in videos if v and v.get("videoId") == int(video_id)),
            None,
        )
        return entity is not None and entity.get("__typename") in _TITLE_TYPENAMES

    def get(self, video_id: str | int) -> LodpTitleAndPlansPageModel:
        """Downloads and parses the LodpTitleAndPlansPage for a given Netflix video ID.

        Args:
            video_id: The numeric Netflix video ID of a Show, also accepts a
            Movie or Episode.

        Returns:
            A LodpTitleAndPlansPage model containing the parsed data.
        """
        return self.parse(self.download(video_id))
