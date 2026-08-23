# TODO: Validate
"""Contains the Meshfilm class."""

from __future__ import annotations

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from meshfilm.detail_modal import DetailModal
from meshfilm.exceptions import HTTPError
from meshfilm.lodp_title_and_plans_page import LodpTitleAndPlansPage
from meshfilm.mini_modal import MiniModal
from meshfilm.preview_modal_episode_selector import PreviewModalEpisodeSelector
from meshfilm.preview_modal_episode_selector_season_episodes import (
    PreviewModalEpisodeSelectorSeasonEpisodes,
)
from meshfilm.preview_modal_video_title_group import PreviewModalVideoTitleGroup
from meshfilm.search_page_results import SearchPageResults

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_URL = "https://web.prod.cloud.netflix.com/graphql"

# The build of the site a request claims to come from.
APP_VERSION = "v232a5da5"


# TODO: Validate
class Meshfilm:
    """Netflix API wrapper."""

    # TODO: Validate
    def __init__(self, get_around_client: GetAround | None = None) -> None:
        """Initialize the Meshfilm client.

        The client holds one attribute per endpoint, so `client.detail_modal(id)`
        looks a title up and `client.detail_modal.download(id)` and
        `client.detail_modal.load(data)` are the halves of it.
        """
        self.get_around_client = get_around_client or GetAround()

        self.lodp_title_and_plans_page = LodpTitleAndPlansPage(self)
        self.preview_modal_episode_selector = PreviewModalEpisodeSelector(self)
        self.preview_modal_episode_selector_season_episodes = (
            PreviewModalEpisodeSelectorSeasonEpisodes(self)
        )
        self.preview_modal_video_title_group = PreviewModalVideoTitleGroup(self)
        self.search_page_results = SearchPageResults(self)
        self.mini_modal = MiniModal(self)
        self.detail_modal = DetailModal(self)

        # Each endpoint is also reachable under a name that says what it answers
        # with instead of the operation Netflix sends it as.
        self.title_page = self.lodp_title_and_plans_page
        self.seasons = self.preview_modal_episode_selector
        self.episodes = self.preview_modal_episode_selector_season_episodes
        self.previews = self.preview_modal_video_title_group
        self.search = self.search_page_results
        self.mini_previews = self.mini_modal
        self.details = self.detail_modal

    # TODO: Validate
    def _headers(self, operation_name: str) -> dict[str, str]:
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            "Origin": "https://www.netflix.com",
            "Referer": "https://www.netflix.com/",
            "x-netflix.context.ui-flavor": "akira",
            "x-netflix.context.app-version": APP_VERSION,
            "x-netflix.context.locales": "en-us",
            "x-netflix.context.operation-name": operation_name,
            "x-netflix.request.attempt": "1",
            "x-netflix.request.client.context": '{"appstate":"foreground"}',
        }

    # TODO: Validate
    def download(self, payload: dict[str, Any], log_id: str) -> str:
        """Post a persisted GraphQL query and return the response body as text.

        A body carrying `errors` is returned rather than raised on, because
        Netflix answers a logged out request with an `UNAUTHENTICATED` error for
        every field that needs an account while still filling in the rest.

        Raises:
            HTTPError: If the request is answered with anything but a 200.
        """
        operation_name: str = payload["operationName"]
        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.post(
            url=API_URL,
            json=payload,
            headers=self._headers(operation_name),
        )

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.text
