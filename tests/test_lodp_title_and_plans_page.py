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
    from meshfilm.lodp_title_and_plans_page import LodpTitleAndPlansPage

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

VIDEO_IDS = [SHOW_ID, EPISODE_ID, MOVIE_ID]
INVALID_IDS = [SEASON_1_ID, SEASON_2_ID, INVALID_ID]


@pytest.fixture(scope="session")
def endpoint() -> LodpTitleAndPlansPage:
    return client.lodp_title_and_plans_page


class TestLodpTitleAndPlansPage:
    def test_alias(self) -> None:
        assert client.title_page is client.lodp_title_and_plans_page

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_download(self, endpoint: LodpTitleAndPlansPage, video_id: int) -> None:
        download_if_missing(
            endpoint,
            str(video_id),
            lambda: endpoint.download(video_id),
        )

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_value(self, endpoint: LodpTitleAndPlansPage, video_id: int) -> None:
        endpoint.parse(json.loads(data_path(endpoint, str(video_id)).read_text()))
        # TODO: assert expected value (needs live data)

    @pytest.mark.parametrize("invalid_id", INVALID_IDS)
    def test_invalid(self, endpoint: LodpTitleAndPlansPage, invalid_id: int) -> None:
        name = str(invalid_id)
        assert_no_content_error(endpoint, name, lambda: endpoint.get(invalid_id))
