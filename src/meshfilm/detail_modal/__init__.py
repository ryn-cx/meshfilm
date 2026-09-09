from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.detail_modal.models import DetailModalModel, model_validate_json
from meshfilm.exceptions import NotATitleError, TitleNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

TITLE_TYPENAMES = frozenset({"Show", "Movie"})
"""What the endpoint answers for, as opposed to a season or an episode of one."""


class DetailModal(BaseEndpoint):
    """Contains information about a specific show.

    - Example Request:
        - URL: https://www.netflix.com/title/81729879

        - Headers:
            - POST /graphql HTTP/2
            - Host: web.prod.cloud.netflix.com
            - User-Agent: __REDACTED__
            - Accept: */*
            - Accept-Language: en-US,en;q=0.9
            - Accept-Encoding: gzip, deflate, br, zstd
            - Referer: https://www.netflix.com/
            - x-netflix.request.id: __REDACTED__
            - content-type: application/json
            - x-netflix.request.toplevel.uuid: __REDACTED__
            - x-netflix.context.ui-flavor: akira
            - x-netflix.request.originating.url: https://www.netflix.com/title/81729879
            - x-netflix.context.hawkins-version: 5.29.0
            - x-netflix.context.app-version: ve2565e1a
            - x-netflix.context.locales: en-US
            - x-netflix.context.operation-name: DetailModal
            - x-netflix.request.attempt: 1
            - x-netflix.request.client.context: {"appstate":"foreground"}
            - Content-Length: 508
            - Origin: https://www.netflix.com
            - Connection: keep-alive
            - Cookie: __REDACTED__
            - Sec-Fetch-Dest: empty
            - Sec-Fetch-Mode: cors
            - Sec-Fetch-Site: same-site
            - Priority: u=4

        - Request:
        {
            "operationName": "DetailModal",
            "variables": {
                "opaqueImageFormat": "JPG",
                "transparentImageFormat": "PNG",
                "videoMerchEnabled": false,
                "fetchPromoVideoOverride": false,
                "hasPromoVideoOverride": false,
                "promoVideoId": 0,
                "videoMerchContext": "BROWSE",
                "isLiveEpisodic": false,
                "includeCroppedLogo": false,
                "artworkContext": {},
                "textEvidenceUiContext": "ODP",
                "unifiedEntityId": "Video:81729879",
                "videoId": 81729879,
                "checkLinearChannel": true
            },
            "extensions": {
                "persistedQuery": {
                "id": "8bb4b13e-a6d6-455a-b821-7ae7804577a4",
                "version": 102
                }
            }
        }
    """

    def __call__(self, title_id: int) -> DetailModalModel:
        """Download and parse the DetailModal file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(title_id), log_id)

    def download(self, title_id: int) -> str:
        """Download the DetailModal file."""
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
                "unifiedEntityId": f"Video:{title_id}",
                "videoId": title_id,
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
        return self._validate_download(response, title_id)

    def _validate_download(self, response: str, title_id: int) -> str:
        entity = json.loads(response)["data"]["unifiedEntities"][0]
        if entity is None:
            raise TitleNotFoundError(title_id, HTTPStatus.OK, response)
        typename = entity["__typename"]
        if typename not in TITLE_TYPENAMES:
            raise NotATitleError(title_id, typename, response)
        return response

    def load(self, data: str, log_id: str = "") -> DetailModalModel:
        """Load a DetailModal file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
