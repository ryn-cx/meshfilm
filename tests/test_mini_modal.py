# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from meshfilm import Meshfilm
    from meshfilm.mini_modal import MiniModal

SHOW_ID = 80095697
"""show_id of Disenchantment."""
SEASON_1_ID = 80117549
"""season_id of Disenchantment Season 1."""
SEASON_2_ID = 80174140
"""season_id of Disenchantment Season 2."""
SEASON_1_EPISODE_IDS: list[str | int] = [
    80117711,
    80145115,
    80145117,
    80145118,
    80145119,
    80145116,
    80145120,
    80145121,
    80145122,
    80145123,
]
"""Every episode from Disenchantment's first season."""
MOVIE_ID = 81458424
""""movie_id of Watch Wake Up Dead Man: A Knives Out Mystery."""

VIDEO_ID_GROUPS: list[list[str | int]] = [
    [SHOW_ID],
    [SEASON_1_ID],
    [SEASON_2_ID],
    [MOVIE_ID],
    SEASON_1_EPISODE_IDS,
]


def _name(video_ids: list[str | int]) -> str:
    return "_".join(str(video_id) for video_id in video_ids)


@pytest.fixture(scope="session")
def endpoint(client: Meshfilm) -> MiniModal:
    return client.mini_modal


class TestMiniModal:
    def test_alias(self, client: Meshfilm) -> None:
        assert client.mini_previews is client.mini_modal

    @pytest.mark.parametrize("video_ids", VIDEO_ID_GROUPS)
    def test_download(self, endpoint: MiniModal, video_ids: list[str | int]) -> None:
        download_and_save(
            endpoint,
            _name(video_ids),
            lambda: endpoint.download(video_ids),
        )

    @pytest.mark.parametrize("video_ids", VIDEO_ID_GROUPS)
    def test_parse(self, endpoint: MiniModal, video_ids: list[str | int]) -> None:
        parse_json(endpoint, _name(video_ids))
        # TODO: assert expected value (needs live data)


@pytest.mark.parametrize("video_ids", VIDEO_ID_GROUPS)
def test_log_id(endpoint: MiniModal, video_ids: list[str | int]) -> None:
    assert endpoint.get_log_id(video_ids) == f"MiniModal video_ids={video_ids!r}"
