# TODO: Validate
"""Contains the LodpTitleAndPlansPage class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import InvalidFileError, VideoNotFoundError
from meshfilm.lodp_title_and_plans_page.models import (
    LodpTitleAndPlansPageModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class LodpTitleAndPlansPage(BaseEndpoint):
    """Manage the logged out details page file.

    The page holds the title itself and the plans it would take to watch it.

    Source: https://www.netflix.com/title/{video_id}

    Example request:
        - POST /graphql
            - HTTP/2
        - Host: web.prod.cloud.netflix.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate
        - Content-Type: application/json
        - Origin: https://www.netflix.com
        - Referer: https://www.netflix.com/
        - x-netflix.context.ui-flavor: akira
        - x-netflix.context.app-version: __REDACTED__
        - x-netflix.context.locales: en-us
        - x-netflix.context.operation-name: LodpTitleAndPlansPageQuery
        - x-netflix.request.attempt: 1
        - x-netflix.request.client.context: {"appstate":"foreground"}
        - Body: the persisted query id for LodpTitleAndPlansPageQuery and the
          video id
    """

    # TODO: Validate
    def __call__(self, video_id: int) -> LodpTitleAndPlansPageModel:
        """Look the title page up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(video_id), log_id)

    # TODO: Validate
    def download(self, video_id: int) -> str:
        """Download the title page file."""
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
            "operationName": "LodpTitleAndPlansPageQuery",
            "variables": {
                "videoId": video_id,
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
        response = self._client.download(payload, log_id)
        return self._validate_download(response, video_id)

    # TODO: Validate
    def _validate_download(self, response: str, video_id: int) -> str:
        video = json.loads(response)["data"]["videos"][0]
        if video is None:
            raise VideoNotFoundError(video_id, HTTPStatus.OK, response)
        if video["videoId"] != video_id:
            raise InvalidFileError(
                field="video id",
                expected=video_id,
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> LodpTitleAndPlansPageModel:
        """Read a downloaded title page file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
