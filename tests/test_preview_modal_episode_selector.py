from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.exceptions import NotAShowError, ShowNotFoundError

if TYPE_CHECKING:
    from meshfilm import Meshfilm

SHOWS = [
    pytest.param(80107103, 37, id="Show"),
    pytest.param(81415953, 0, id="Deleted Show"),
]

NOT_SHOWS = [
    pytest.param(81458424, id="Movie"),
    pytest.param(81159422, id="Episode"),
]


@pytest.mark.parametrize(("show_id", "season_count"), SHOWS)
def test_download(client: Meshfilm, show_id: int, season_count: int) -> None:
    show = client.preview_modal_episode_selector(show_id, season_count)
    assert show.video_id == show_id
    assert len(show.seasons.edges) == season_count


@pytest.mark.parametrize(("show_id", "season_count"), SHOWS)
def test_download_no_season_count(
    client: Meshfilm,
    show_id: int,
    season_count: int,
) -> None:
    show = client.preview_modal_episode_selector(show_id)
    assert show.video_id == show_id
    assert len(show.seasons.edges) == season_count


def test_download_invalid(client: Meshfilm) -> None:
    with pytest.raises(ShowNotFoundError):
        client.preview_modal_episode_selector.download(1)


# TODO: Validate
@pytest.mark.parametrize("video_id", NOT_SHOWS)
def test_download_not_a_show(client: Meshfilm, video_id: int) -> None:
    with pytest.raises(NotAShowError):
        client.preview_modal_episode_selector.download(video_id)
