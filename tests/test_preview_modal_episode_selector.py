# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from get_around import build_client_automatically

from meshfilm import Meshfilm
from tests.utils import (
    assert_no_content_error,
    data_path,
    download_if_missing,
)

if TYPE_CHECKING:
    from meshfilm.preview_modal_episode_selector import PreviewModalEpisodeSelector

client = Meshfilm(build_client_automatically())

SHOW_ID = 80095697
"""show_id of Disenchantment."""
SEASON_1_ID = 80117549
"""season_id of Disenchantment Season 1."""
SEASON_2_ID = 80174140
"""season_id of Disenchantment Season 2."""
EPISODE_ID = 80117711
"""episode_id of Disenchantment Season 1 Episode 1."""
INVALID_ID = 1
MOVIE_ID = 81458424
""""movie_id of Watch Wake Up Dead Man: A Knives Out Mystery."""

INVALID_IDS = [SEASON_1_ID, SEASON_2_ID, EPISODE_ID, MOVIE_ID, INVALID_ID]


@pytest.fixture(scope="session")
def endpoint() -> PreviewModalEpisodeSelector:
    return client.preview_modal_episode_selector


class TestPreviewModalEpisodeSelector:
    def test_alias(self) -> None:
        assert client.seasons is client.preview_modal_episode_selector

    def test_download(self, endpoint: PreviewModalEpisodeSelector) -> None:
        download_if_missing(
            endpoint,
            str(SHOW_ID),
            lambda: endpoint.download(SHOW_ID),
        )

    def test_value(self, endpoint: PreviewModalEpisodeSelector) -> None:
        endpoint.parse(json.loads(data_path(endpoint, str(SHOW_ID)).read_text()))
        # TODO: assert expected value (needs live data)

    @pytest.mark.parametrize("invalid_id", INVALID_IDS)
    def test_invalid(
        self,
        endpoint: PreviewModalEpisodeSelector,
        invalid_id: int,
    ) -> None:
        name = str(invalid_id)
        assert_no_content_error(endpoint, name, lambda: endpoint.get(invalid_id))
