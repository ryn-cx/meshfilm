from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.exceptions import NotASeasonError, SeasonNotFoundError
from meshfilm.preview_modal_episode_selector_season_episodes import (
    LATER_PAGES_EPISODE_COUNT,
    PAGE_1_EPISODE_COUNT,
)

if TYPE_CHECKING:
    from meshfilm import Meshfilm

SEASONS = [pytest.param(81159306, 118, id="Season")]

NOT_SEASONS = [
    pytest.param(80107103, id="Show"),
    pytest.param(81458424, id="Movie"),
    pytest.param(81159422, id="Episode"),
]


@pytest.mark.parametrize(("season_id", "episode_count"), SEASONS)
def test_download(client: Meshfilm, season_id: int, episode_count: int) -> None:
    endpoint = client.preview_modal_episode_selector_season_episodes
    first_page = endpoint(season_id)
    assert first_page.data.videos[0].video_id == season_id
    first_page_episode_count = min(PAGE_1_EPISODE_COUNT, episode_count)
    first_page_episodes = first_page.data.videos[0].episodes
    assert len(first_page_episodes.edges) == first_page_episode_count

    remaining_episode_count = episode_count - first_page_episode_count
    assert first_page_episodes.page_info.has_next_page == (remaining_episode_count > 0)
    if remaining_episode_count == 0:
        return

    second_page = endpoint(season_id, first_page_episodes.page_info.end_cursor)
    assert second_page.data.videos[0].video_id == season_id
    second_page_episodes = second_page.data.videos[0].episodes
    assert len(second_page_episodes.edges) == min(
        LATER_PAGES_EPISODE_COUNT,
        remaining_episode_count,
    )


@pytest.mark.parametrize(("season_id", "episode_count"), SEASONS)
def test_download_all(client: Meshfilm, season_id: int, episode_count: int) -> None:
    endpoint = client.preview_modal_episode_selector_season_episodes
    downloaded_episode_count = 0
    for page in endpoint.load_pages(endpoint.download_all(season_id)):
        episodes = page.data.videos[0].episodes
        downloaded_episode_count += len(episodes.edges)

    assert downloaded_episode_count == episode_count


def test_download_invalid(client: Meshfilm) -> None:
    with pytest.raises(SeasonNotFoundError):
        client.preview_modal_episode_selector_season_episodes.download(1)


# TODO: Validate
@pytest.mark.parametrize("video_id", NOT_SEASONS)
def test_download_not_a_season(client: Meshfilm, video_id: int) -> None:
    with pytest.raises(NotASeasonError):
        client.preview_modal_episode_selector_season_episodes.download(video_id)
