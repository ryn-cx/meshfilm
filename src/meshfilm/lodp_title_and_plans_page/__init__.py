from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import TitleNotFoundError
from meshfilm.lodp_title_and_plans_page.models import (
    LodpTitleAndPlansPageModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_video(response: str) -> dict[str, Any]:
    """Extract the video from the LodpTitleAndPlansPage response."""
    if video := json.loads(response)["data"]["videos"][0]:
        return video

    raise TitleNotFoundError(HTTPStatus.OK, response)


# TODO: Validate
class LodpTitleAndPlansPage(BaseEndpoint):
    """Contains the logged out details page for a specific title.

    The page holds the title itself, the plans it would take to watch it, and
    the titles Netflix considers similar to it.

    - Example Request:
        - URL: https://www.netflix.com/title/80240027

        - Headers:
            - POST /graphql HTTP/2
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

        - Request:
        {
            "operationName": "LodpTitleAndPlansPageQuery",
            "variables": {
                "videoId": 80240027,
                "opaqueImageFormat": "JPG",
                "transparentImageFormat": "PNG",
                "thumbnailVideoId": -1,
                "hasValidThumbnailVideoId": false,
                "useBakedInPlayThumbnail": false,
                "useFromWatchSupplements": false
            },
            "extensions": {
                "persistedQuery": {
                "id": "807ffc59-06c3-45b1-bd84-b9b4136381fc",
                "version": 102
                }
            }
        }
    """

    # TODO: Validate
    def __call__(self, title_id: int) -> LodpTitleAndPlansPageModel:
        """Download and parse the LodpTitleAndPlansPage file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(title_id), log_id)

    # TODO: Validate
    def download(self, title_id: int) -> str:
        """Download the LodpTitleAndPlansPage file."""
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
            "operationName": "LodpTitleAndPlansPageQuery",
            "variables": {
                "videoId": title_id,
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
        extract_video(response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> LodpTitleAndPlansPageModel:
        """Load a LodpTitleAndPlansPage file into its model."""
        return model_validate_json(extract_video(data), log_id or self.default_log_id)
