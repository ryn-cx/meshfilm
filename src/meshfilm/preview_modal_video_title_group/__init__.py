# TODO: Validate
"""Contains the PreviewModalVideoTitleGroup class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import InvalidFileError
from meshfilm.preview_modal_video_title_group.models import (
    PreviewModalVideoTitleGroupModel,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class PreviewModalVideoTitleGroup(BaseEndpoint[PreviewModalVideoTitleGroupModel]):
    """Manage the preview modal video title group file."""

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
        """Downloads the preview modal video title group file."""
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            self._payload(video_ids),
            log_id=log_id,
        )
        # Unavailable ids are dropped from the response, so the returned ids only
        # have to be some of the requested ones.
        videos = data.get("data", {}).get("videos") or []
        found = {video.get("videoId") for video in videos}
        if not found or not found <= {int(video_id) for video_id in video_ids}:
            raise InvalidFileError(field="video ids", expected=video_ids)
        return data

    def download_and_parse(
        self,
        video_ids: list[str | int],
    ) -> PreviewModalVideoTitleGroupModel:
        """Downloads and parses the preview modal video title group file."""
        return self.parse(self.download(video_ids))
