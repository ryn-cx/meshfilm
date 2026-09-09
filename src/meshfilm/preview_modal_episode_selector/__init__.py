from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import NotAShowError, ShowNotFoundError
from meshfilm.preview_modal_episode_selector.models import (
    PreviewModalEpisodeSelectorModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class PreviewModalEpisodeSelector(BaseEndpoint):
    """Contains information about a show's seasons.

    - Example Request:
        - URL: https://www.netflix.com/title/80107103

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
            - x-netflix.request.originating.url: https://www.netflix.com/title/80107103
            - x-netflix.context.hawkins-version: 5.29.0
            - x-netflix.context.app-version: ve2565e1a
            - x-netflix.context.locales: en-US
            - x-netflix.context.operation-name: PreviewModalEpisodeSelector
            - x-netflix.request.attempt: 1
            - x-netflix.request.client.context: {"appstate":"foreground"}
            - Content-Length: 188
            - Origin: https://www.netflix.com
            - Connection: keep-alive
            - Cookie: __REDACTED__
            - Sec-Fetch-Dest: empty
            - Sec-Fetch-Mode: cors
            - Sec-Fetch-Site: same-site
            - Priority: u=4
            - TE: trailers

        - Request:
        {
            "operationName": "PreviewModalEpisodeSelector",
            "variables": {
                "showId": 80107103,
                "seasonCount": 37
            },
            "extensions": {
                "persistedQuery": {
                "id": "dbc3b274-d4f9-4811-aaf1-d082d3b936f2",
                "version": 102
                }
            }
        }
    """

    def __call__(
        self,
        show_id: int,
        season_count: int = 100,
    ) -> PreviewModalEpisodeSelectorModel:
        """Download and parse the PreviewModalEpisodeSelector file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(show_id, season_count), log_id)

    def download(self, show_id: int, season_count: int | None = None) -> str:
        """Download the PreviewModalEpisodeSelector file.

        Args:
            show_id: The ID of the show.
            season_count: The number of seasons to fetch. Official requests match the
            total number of seasons, but as an alternative a default of 100 will fetch
            all seasons if it is not provided.
        """
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
            "operationName": "PreviewModalEpisodeSelector",
            "variables": {
                "showId": show_id,
                # It's best to include the exact value for season_count to match the
                # official requests as close as possible but a default of 100 will get
                # all of the seasons if doing that is too much work.
                "seasonCount": 100 if season_count is None else season_count,
            },
            "extensions": {
                "persistedQuery": {
                    "id": "dbc3b274-d4f9-4811-aaf1-d082d3b936f2",
                    "version": 102,
                },
            },
        }
        headers = {
            "x-netflix.request.originating.url": (
                f"https://www.netflix.com/title/{show_id}"
            ),
        }
        response = self._client.download(payload, log_id, headers)
        return self._validate_download(response, show_id)

    def _validate_download(self, response: str, show_id: int) -> str:
        video = json.loads(response)["data"]["videos"][0]
        if video is None:
            raise ShowNotFoundError(show_id, HTTPStatus.OK, response)
        typename = video["__typename"]
        if typename != "Show":
            raise NotAShowError(show_id, typename, response)
        return response

    def load(self, data: str, log_id: str = "") -> PreviewModalEpisodeSelectorModel:
        """Load a PreviewModalEpisodeSelector file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
