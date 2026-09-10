from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import NotASeasonError, SeasonNotFoundError
from meshfilm.preview_modal_episode_selector_season_episodes.models import (
    PreviewModalEpisodeSelectorSeasonEpisodesModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PAGE_1_EPISODE_COUNT = 30
LATER_PAGES_EPISODE_COUNT = 50


# TODO: Validate
def extract_season(page: str) -> dict[str, Any]:
    """Extract the season data from one page of the response."""
    if season := json.loads(page)["data"]["videos"][0]:
        return season

    raise SeasonNotFoundError(HTTPStatus.OK, page)


# TODO: Validate
def _validate_download(response: str, season_id: int) -> str:
    typename = extract_season(response)["__typename"]
    if typename != "Season":
        raise NotASeasonError(season_id, typename, response)
    return response


class PreviewModalEpisodeSelectorSeasonEpisodes(BaseEndpoint):
    """Contains the episodes of one season, a page at a time.

    - Example Request (first page):
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
            - x-netflix.context.operation-name:
              PreviewModalEpisodeSelectorSeasonEpisodes
            - x-netflix.request.attempt: 1
            - x-netflix.request.client.context: {"appstate":"foreground"}
            - Content-Length: 244
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
            "operationName": "PreviewModalEpisodeSelectorSeasonEpisodes",
            "variables": {
                "seasonId": 81015581,
                "count": 30,
                "opaqueImageFormat": "JPG",
                "artworkContext": {}
            },
            "extensions": {
                "persistedQuery": {
                "id": "4cf0a279-dd32-454d-9758-486359c0d48b",
                "version": 102
                }
            }
        }

    - Example Request (every page after the first):
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
            - x-netflix.context.operation-name:
              PreviewModalEpisodeSelectorSeasonEpisodes
            - x-netflix.request.attempt: 1
            - x-netflix.request.client.context: {"appstate":"foreground"}
            - Content-Length: 260
            - Origin: https://www.netflix.com
            - Connection: keep-alive
            - Cookie: __REDACTED__
            - Sec-Fetch-Dest: empty
            - Sec-Fetch-Mode: cors
            - Sec-Fetch-Site: same-site

        - Request:
        {
            "operationName": "PreviewModalEpisodeSelectorSeasonEpisodes",
            "variables": {
                "seasonId": 80107104,
                "count": 50,
                "opaqueImageFormat": "JPG",
                "artworkContext": {},
                "cursor": "Mjk="
            },
            "extensions": {
                "persistedQuery": {
                "id": "4cf0a279-dd32-454d-9758-486359c0d48b",
                "version": 102
                }
            }
        }
    """

    def __call__(
        self,
        season_id: int,
        cursor: str | None = None,
        count: int | None = None,
    ) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
        """Download and parse the PreviewModalEpisodeSelectorSeasonEpisodes file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(season_id, cursor, count), log_id)

    def download(
        self,
        season_id: int,
        cursor: str | None = None,
        count: int | None = None,
    ) -> str:
        """Download the PreviewModalEpisodeSelectorSeasonEpisodes file."""
        log_id = self.get_log_id(self.download, locals())
        if count is None:
            count = (
                PAGE_1_EPISODE_COUNT if cursor is None else LATER_PAGES_EPISODE_COUNT
            )
        variables: dict[str, Any] = {
            "seasonId": season_id,
            "count": count,
            "opaqueImageFormat": "JPG",
            "artworkContext": {},
        }
        if cursor is not None:
            variables["cursor"] = cursor
        payload: dict[str, Any] = {
            "operationName": "PreviewModalEpisodeSelectorSeasonEpisodes",
            "variables": variables,
            "extensions": {
                "persistedQuery": {
                    "id": "27b30e4e-871d-46aa-ac8b-244103d2e37d",
                    "version": 102,
                },
            },
        }
        response = self._client.download(payload, log_id)
        return _validate_download(response, season_id)

    def download_all(self, season_id: int) -> list[str]:
        """Download all PreviewModalEpisodeSelectorSeasonEpisodes files for a season."""
        pages: list[str] = []
        cursor: str | None = None

        while True:
            page = self.download(season_id, cursor)
            pages.append(page)
            page_info = self._page_info(page)
            if not page_info["hasNextPage"]:
                return pages
            cursor = page_info["endCursor"]

    # TODO: Validate
    @staticmethod
    def _page_info(page: str) -> dict[str, Any]:
        """Return the paging of one page."""
        return extract_season(page)["episodes"]["pageInfo"]

    # TODO: Validate
    def load(
        self,
        data: str,
        log_id: str = "",
    ) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
        """Load the season of a PreviewModalEpisodeSelectorSeasonEpisodes file."""
        return model_validate_json(extract_season(data), log_id or self.default_log_id)

    def load_pages(
        self,
        pages: list[str],
    ) -> list[PreviewModalEpisodeSelectorSeasonEpisodesModel]:
        """Load PreviewModalEpisodeSelectorSeasonEpisodes files into their models."""
        return [self.load(page) for page in pages]
