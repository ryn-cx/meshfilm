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
"""How many episodes the site itself asks for."""


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
          PreviewModalEpisodeSelectorSeasonEpisodes, the season id and how many
          episodes to return
    """

    # TODO: Validate
    def __call__(
        self,
        season_id: int,
        count: int = EPISODE_COUNT,
    ) -> PreviewModalEpisodeSelectorSeasonEpisodesModel:
        """Look the season's episodes up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(season_id, count), log_id)

    # TODO: Validate
    def download(self, season_id: int, count: int = EPISODE_COUNT) -> str:
        """Download the season episodes file."""
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
            "operationName": "PreviewModalEpisodeSelectorSeasonEpisodes",
            "variables": {
                "seasonId": season_id,
                "count": count,
                "opaqueImageFormat": "JPG",
                "artworkContext": {},
            },
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
