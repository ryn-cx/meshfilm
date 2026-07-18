# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from meshfilm import Meshfilm
    from meshfilm.detail_modal import DetailModal

SHOW_ID = 80095697
"""show_id of Disenchantment."""
SEASON_1_ID = 80117549
"""season_id of Disenchantment Season 1."""
SEASON_2_ID = 80174140
"""season_id of Disenchantment Season 2."""
EPISODE_ID = 80117711
"""episode_id of Disenchantment Season 1 Episode 1."""
MOVIE_ID = 81458424
""""movie_id of Watch Wake Up Dead Man: A Knives Out Mystery."""

VIDEO_IDS = [EPISODE_ID, SHOW_ID, SEASON_1_ID, SEASON_2_ID, MOVIE_ID]


@pytest.fixture(scope="session")
def endpoint(client: Meshfilm) -> DetailModal:
    return client.detail_modal


class TestDetailModal:
    def test_alias(self, client: Meshfilm) -> None:
        assert client.details is client.detail_modal

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_download(self, endpoint: DetailModal, video_id: int) -> None:
        download_and_save(
            endpoint,
            str(video_id),
            lambda: endpoint.download(video_id),
        )

    @pytest.mark.parametrize("video_id", VIDEO_IDS)
    def test_parse(self, endpoint: DetailModal, video_id: int) -> None:
        parse_json(endpoint, str(video_id))
        # TODO: assert expected value (needs live data)


@pytest.mark.parametrize("video_id", VIDEO_IDS)
def test_log_id(endpoint: DetailModal, video_id: int) -> None:
    assert endpoint.get_log_id(video_id) == f"DetailModal video_id={video_id!r}"
