# TODO: Validate
"""Contains the PreviewModalEpisodeSelectorSeasonEpisodes class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import InvalidFileError, SeasonNotFoundError
from meshfilm.preview_modal_episode_selector_season_episodes.models import (
    PreviewModalEpisodeSelectorSeasonEpisodesModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

EPISODE_COUNT = 30
"""How many episodes the site itself asks for on the first page."""

LATER_EPISODE_COUNT = 50
"""How many episodes the site itself asks for on every page after the first."""


# TODO: Validate
class PreviewModalEpisodeSelectorSeasonEpisodes(BaseEndpoint):
    """Manage the season episodes file, which holds the episodes of one season.

    Source: https://www.netflix.com/title/{show_id}

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
        - x-netflix.context.operation-name:
          PreviewModalEpisodeSelectorSeasonEpisodes
        - x-netflix.request.attempt: 1
        - x-netflix.request.client.context: {"appstate":"foreground"}
        - Body: the persisted query id for
          PreviewModalEpisodeSelectorSeasonEpisodes, the season id, how many
          episodes to return and the cursor to start after
    """

    # TODO: Validate
    def __call__(
        self,
        season_id: int,
        count: int = EPISODE_COUNT,
        cursor: str | None = None,
    ) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
        """Look the season's episodes up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(season_id, count, cursor), log_id)

    # TODO: Validate
    def download(
        self,
        season_id: int,
        count: int = EPISODE_COUNT,
        cursor: str | None = None,
    ) -> str:
        """Download one page of the season episodes file.

        The page starts after `cursor`, which is the `endCursor` of the page
        before it. Without one it starts at the first episode.
        """
        log_id = self.get_log_id(self.download, locals())
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
        return self._validate_download(response, season_id)

    # TODO: Validate
    def download_all(
        self,
        season_id: int,
        first_page_count: int = EPISODE_COUNT,
        later_page_count: int = LATER_EPISODE_COUNT,
    ) -> list[str]:
        """Download every page of a season's episodes.

        The first page asks for fewer episodes than the ones after it, which is
        what the site itself does.
        """
        pages: list[str] = []
        cursor: str | None = None

        while True:
            count = first_page_count if not pages else later_page_count
            page = self.download(season_id, count, cursor)
            pages.append(page)
            page_info = self._page_info(page)
            if page_info is None or not page_info["hasNextPage"]:
                return pages
            cursor = page_info["endCursor"]

    # TODO: Validate
    def download_merged(
        self,
        season_id: int,
        first_page_count: int = EPISODE_COUNT,
        later_page_count: int = LATER_EPISODE_COUNT,
    ) -> str:
        """Download every page of a season's episodes as a single file."""
        return self.merge_pages(
            self.download_all(season_id, first_page_count, later_page_count),
        )

    # TODO: Validate
    @staticmethod
    def _page_info(page: str) -> dict[str, Any] | None:
        """Return the paging of one page, or None when it holds no episodes.

        A movie is answered with itself and no episodes at all, so there is
        nothing to page through.
        """
        episodes = json.loads(page)["data"]["videos"][0].get("episodes")
        return None if episodes is None else episodes["pageInfo"]

    # TODO: Validate
    @staticmethod
    def merge_pages(pages: list[str]) -> str:
        """Return the pages of one season written out as a single file.

        The first page is what the merged file is built on, since everything it
        says around the episodes is what the season is, and its episode edges
        are replaced by the edges of every page in the order they were served.
        The paging of the last page is kept, so the merged file says where the
        walk ended.

        Raises:
            ValueError: If there are no pages, since there is nothing to say the
                season was answered with.
        """
        if not pages:
            msg = "Expected at least one page, got none."
            raise ValueError(msg)

        merged = json.loads(pages[0])
        episodes = merged["data"]["videos"][0].get("episodes")
        if episodes is None:
            return json.dumps(merged)

        episodes["edges"] = [
            edge
            for page in pages
            for edge in json.loads(page)["data"]["videos"][0]["episodes"]["edges"]
        ]
        episodes["pageInfo"] = json.loads(pages[-1])["data"]["videos"][0]["episodes"][
            "pageInfo"
        ]
        return json.dumps(merged)

    # TODO: Validate
    def _validate_download(self, response: str, season_id: int) -> str:
        video = json.loads(response)["data"]["videos"][0]
        if video is None:
            raise SeasonNotFoundError(season_id, HTTPStatus.OK, response)
        if video["videoId"] != season_id:
            raise InvalidFileError(
                field="season id",
                expected=season_id,
                response=response,
            )
        return response

    # TODO: Validate
    def load(
        self,
        data: str,
        log_id: str = "",
    ) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
        """Read a downloaded season episodes file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    def load_pages(
        self,
        pages: list[str],
    ) -> list[PreviewModalEpisodeSelectorSeasonEpisodesModel]:
        """Read the pages `download_all` returns into their models."""
        return [self.load(page) for page in pages]
