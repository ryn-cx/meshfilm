"""Netflix API wrapper."""

from __future__ import annotations

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any
from uuid import uuid4

from get_around import GetAround

from meshfilm.detail_modal import DetailModal
from meshfilm.exceptions import HTTPError
from meshfilm.lodp_title_and_plans_page import LodpTitleAndPlansPage
from meshfilm.preview_modal_episode_selector import PreviewModalEpisodeSelector
from meshfilm.preview_modal_episode_selector_season_episodes import (
    PreviewModalEpisodeSelectorSeasonEpisodes,
)
from meshfilm.search_page_query_results import SearchPageQueryResults

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Meshfilm:
    """Netflix API wrapper."""

    def __init__(self, get_around_client: GetAround | None = None) -> None:
        """Initialize the Meshfilm client."""
        self.get_around_client = get_around_client or GetAround()

        self.preview_modal_episode_selector = PreviewModalEpisodeSelector(self)
        self.preview_modal_episode_selector_season_episodes = (
            PreviewModalEpisodeSelectorSeasonEpisodes(self)
        )
        self.search_page_query_results = SearchPageQueryResults(self)
        self.detail_modal = DetailModal(self)
        self.lodp_title_and_plans_page = LodpTitleAndPlansPage(self)

        # Alternative API interface.
        self.title = self.detail_modal
        self.seasons = self.preview_modal_episode_selector
        self.episodes = self.preview_modal_episode_selector_season_episodes
        self.search = self.search_page_query_results
        self.similar = self.lodp_title_and_plans_page

    def _headers(self, operation_name: str) -> dict[str, str]:
        """Build the headers the browser sends, in the order it sends them."""
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            # The browser also offers br and zstd, but httpx can only decode those
            # with brotli and zstandard installed.
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://www.netflix.com/",
            "Content-Type": "application/json",
            "x-netflix.request.toplevel.uuid": str(uuid4()),
            "x-netflix.context.ui-flavor": "akira",
            "x-netflix.context.hawkins-version": "5.29.0",
            "x-netflix.context.app-version": "ve2565e1a",
            "x-netflix.context.locales": "en-US",
            "x-netflix.context.operation-name": operation_name,
            "x-netflix.request.attempt": "1",
            "x-netflix.request.client.context": '{"appstate":"foreground"}',
            "Origin": "https://www.netflix.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Priority": "u=4",
        }

    def download(
        self,
        payload: dict[str, Any],
        log_id: str,
        headers: dict[str, str] | None = None,
    ) -> str:
        """Download from the graphql endpoint."""
        operation_name = payload["operationName"]
        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.post(
            url="https://web.prod.cloud.netflix.com/graphql",
            json=payload,
            headers=self._headers(operation_name) | (headers or {}),
        )

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.text
