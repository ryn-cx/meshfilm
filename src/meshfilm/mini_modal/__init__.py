# TODO: Validate
"""Contains the MiniModal class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import InvalidFileError
from meshfilm.mini_modal.models import MiniModalModel, model_validate_json

if TYPE_CHECKING:
    from collections.abc import Sequence

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MiniModal(BaseEndpoint):
    """Manage the mini modal file, the hover card for a batch of titles.

    Source: https://www.netflix.com/browse

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
        - x-netflix.context.operation-name: MiniModalQuery
        - x-netflix.request.attempt: 1
        - x-netflix.request.client.context: {"appstate":"foreground"}
        - Body: the persisted query id for MiniModalQuery and the video ids
    """

    # TODO: Validate
    def __call__(self, video_ids: Sequence[int]) -> MiniModalModel:
        """Look the hover cards up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(video_ids), log_id)

    # TODO: Validate
    def download(self, video_ids: Sequence[int]) -> str:
        """Download the mini modal file."""
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
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
        response = self._client.download(payload, log_id)
        return self._validate_download(response, video_ids)

    # TODO: Validate
    def _validate_download(self, response: str, video_ids: Sequence[int]) -> str:
        entities = json.loads(response)["data"]["unifiedEntities"]
        # An id nothing is under keeps its place in the answer as a null, so
        # only some of what was asked for has to come back.
        returned_ids = {entity["videoId"] for entity in entities if entity}
        if not returned_ids <= set(video_ids):
            raise InvalidFileError(
                field="video ids",
                expected=list(video_ids),
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MiniModalModel:
        """Read a downloaded mini modal file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
