# TODO: Validate
"""Contains the DetailModal class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.detail_modal.models import DetailModalModel, model_validate_json
from meshfilm.exceptions import InvalidFileError, VideoNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class DetailModal(BaseEndpoint):
    """Manage the detail modal file.

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
        - x-netflix.context.operation-name: DetailModal
        - x-netflix.request.attempt: 1
        - x-netflix.request.client.context: {"appstate":"foreground"}
        - Body: the persisted query id for DetailModal and the video id
    """

    # TODO: Validate
    def __call__(self, video_id: int) -> DetailModalModel:
        """Look the title up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(video_id), log_id)

    # TODO: Validate
    def download(self, video_id: int) -> str:
        """Download the detail modal file."""
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
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
                "videoId": video_id,
                "checkLinearChannel": True,
            },
            "extensions": {
                "persistedQuery": {
                    "id": "8bb4b13e-a6d6-455a-b821-7ae7804577a4",
                    "version": 102,
                },
            },
        }
        response = self._client.download(payload, log_id)
        return self._validate_download(response, video_id)

    # TODO: Validate
    def _validate_download(self, response: str, video_id: int) -> str:
        entity = json.loads(response)["data"]["unifiedEntities"][0]
        if entity is None:
            raise VideoNotFoundError(video_id, HTTPStatus.OK, response)
        if entity["videoId"] != video_id:
            raise InvalidFileError(
                field="video id",
                expected=video_id,
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> DetailModalModel:
        """Read a downloaded detail modal file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
