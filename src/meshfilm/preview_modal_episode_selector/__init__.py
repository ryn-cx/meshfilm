# TODO: Validate
"""Contains the PreviewModalEpisodeSelector class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from meshfilm.base_api_endpoint import BaseEndpoint
from meshfilm.exceptions import InvalidFileError, ShowNotFoundError
from meshfilm.preview_modal_episode_selector.models import (
    PreviewModalEpisodeSelectorModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

SEASON_COUNT = 5
"""How many seasons the site itself asks for."""


# TODO: Validate
class PreviewModalEpisodeSelector(BaseEndpoint):
    """Manage the season selector file, which holds the seasons of one show.

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
        - x-netflix.context.operation-name: PreviewModalEpisodeSelector
        - x-netflix.request.attempt: 1
        - x-netflix.request.client.context: {"appstate":"foreground"}
        - Body: the persisted query id for PreviewModalEpisodeSelector, the show
          id and how many seasons to return
    """

    # TODO: Validate
    def __call__(
        self,
        show_id: int,
        season_count: int = SEASON_COUNT,
    ) -> PreviewModalEpisodeSelectorModel:
        """Look the show's seasons up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(show_id, season_count), log_id)

    # TODO: Validate
    def download(self, show_id: int, season_count: int = SEASON_COUNT) -> str:
        """Download the season selector file."""
        log_id = self.get_log_id(self.download, locals())
        payload: dict[str, Any] = {
            "operationName": "PreviewModalEpisodeSelector",
            "variables": {
                "showId": show_id,
                "seasonCount": season_count,
            },
            "extensions": {
                "persistedQuery": {
                    "id": "dbc3b274-d4f9-4811-aaf1-d082d3b936f2",
                    "version": 102,
                },
            },
        }
        response = self._client.download(payload, log_id)
        return self._validate_download(response, show_id)

    # TODO: Validate
    def _validate_download(self, response: str, show_id: int) -> str:
        video = json.loads(response)["data"]["videos"][0]
        if video is None:
            raise ShowNotFoundError(show_id, HTTPStatus.OK, response)
        if video["videoId"] != show_id:
            raise InvalidFileError(field="show id", expected=show_id, response=response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> PreviewModalEpisodeSelectorModel:
        """Read a downloaded season selector file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
