"""Netflix API wrapper."""

from __future__ import annotations

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

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

if TYPE_CHECKING:
    from httpx import Response

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Meshfilm:
    """Netflix API wrapper."""

    def __init__(self, get_around_client: GetAround | None = None) -> None:
        """Initialize the meshfilm client.

        Args:
            get_around_client: The HTTP client used for every request.
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

        self.title_page = self.lodp_title_and_plans_page
        self.seasons = self.preview_modal_episode_selector
        self.episodes = self.preview_modal_episode_selector_season_episodes
        self.previews = self.preview_modal_video_title_group
        self.search = self.search_page_results
        self.mini_previews = self.mini_modal
        self.details = self.detail_modal

    def _headers(self, payload: dict[str, Any]) -> dict[str, str]:
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
            "x-netflix.context.app-version": "v232a5da5",
            "x-netflix.context.locales": "en-us",
            "x-netflix.context.operation-name": payload["operationName"],
            "x-netflix.request.attempt": "1",
            "x-netflix.request.client.context": '{"appstate":"foreground"}',
        }

    def _download_response(
        self,
        headers: dict[str, str],
        body: dict[str, Any],
        log_id: object = None,
    ) -> Response:
        operation = f"{body.get('operationName')} ({log_id})"
        logger.debug("Downloading: %s", operation)
        start = time.monotonic()
        response = self.get_around_client.post(
            url="https://web.prod.cloud.netflix.com/graphql",
            json=body,
            headers=headers,
        )

        if response.status_code != HTTPStatus.OK:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        logger.debug("Downloaded %s (%.4f s)", operation, time.monotonic() - start)

        return response

    def download(
        self,
        payload: dict[str, Any],
        log_id: object = None,
    ) -> dict[str, Any]:
        """Post a GraphQL query and return its response with request metadata.

        Args:
            payload: The GraphQL request payload.
            log_id: An identifier for the request (e.g. the video or season ID)
                included in log messages to distinguish requests.

        Returns:
            The raw GraphQL response, suitable for passing to `parse()`.
        """
        response = self._download_response(
            headers=self._headers(payload),
            body=payload,
            log_id=log_id,
        )
        return response.json()
