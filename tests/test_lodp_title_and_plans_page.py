# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from meshfilm import Meshfilm
    from meshfilm.lodp_title_and_plans_page import LodpTitleAndPlansPage

SHOW_ID = 80095697
"""show_id of Disenchantment."""
EPISODE_ID = 80117711
"""episode_id of Disenchantment Season 1 Episode 1."""
MOVIE_ID = 81458424
""""movie_id of Watch Wake Up Dead Man: A Knives Out Mystery."""

VIDEO_IDS = [SHOW_ID, EPISODE_ID, MOVIE_ID]


@pytest.fixture(scope="session")
def endpoint(client: Meshfilm) -> LodpTitleAndPlansPage:
    return client.lodp_title_and_plans_page


class TestLodpTitleAndPlansPage:
    def test_alias(self, client: Meshfilm) -> None:
        assert client.title_page is client.lodp_title_and_plans_page

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_download(self, endpoint: LodpTitleAndPlansPage, video_id: int) -> None:
        download_and_save(
            endpoint,
            str(video_id),
            lambda: endpoint.download(video_id),
        )

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_parse(self, endpoint: LodpTitleAndPlansPage, video_id: int) -> None:
        parse_json(endpoint, str(video_id))
        # TODO: assert expected value (needs live data)


@pytest.mark.parametrize("video_id", VIDEO_IDS)
def test_log_id(endpoint: LodpTitleAndPlansPage, video_id: int) -> None:
    expected = f"LodpTitleAndPlansPage video_id={video_id!r}"
    assert endpoint.get_log_id(video_id) == expected
