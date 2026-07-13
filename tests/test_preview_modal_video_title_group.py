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
    from meshfilm.preview_modal_video_title_group import PreviewModalVideoTitleGroup

client = Meshfilm(build_client_automatically())

SHOW_ID = 80095697
"""show_id of Disenchantment."""
SEASON_1_ID = 80117549
"""season_id of Disenchantment Season 1."""
SEASON_2_ID = 80174140
"""season_id of Disenchantment Season 2."""
INVALID_ID = 1
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
def endpoint() -> PreviewModalVideoTitleGroup:
    return client.preview_modal_video_title_group


class TestPreviewModalVideoTitleGroup:
    def test_alias(self) -> None:
        assert client.previews is client.preview_modal_video_title_group

    @pytest.mark.parametrize("video_ids", VIDEO_ID_GROUPS)
    def test_download(
        self,
        endpoint: PreviewModalVideoTitleGroup,
        video_ids: list[str | int],
    ) -> None:
        download_if_missing(
            endpoint,
            _name(video_ids),
            lambda: endpoint.download(video_ids),
        )

    @pytest.mark.parametrize("video_ids", VIDEO_ID_GROUPS)
    def test_value(
        self,
        endpoint: PreviewModalVideoTitleGroup,
        video_ids: list[str | int],
    ) -> None:
        endpoint.parse(json.loads(data_path(endpoint, _name(video_ids)).read_text()))
        # TODO: assert expected value (needs live data)

    def test_invalid(self, endpoint: PreviewModalVideoTitleGroup) -> None:
        name = _name([INVALID_ID])
        assert_no_content_error(endpoint, name, lambda: endpoint.get([INVALID_ID]))
