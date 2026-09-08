# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.exceptions import SeasonNotFoundError
from meshfilm.preview_modal_episode_selector_season_episodes import EPISODE_COUNT
from meshfilm.preview_modal_episode_selector_season_episodes.models import (
    PreviewModalEpisodeSelectorSeasonEpisodesModel,
)
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from meshfilm import Meshfilm

# Each season is asked for with the number of episodes to return, and both are
# part of the name the response is recorded under.
SEASONS = [
    # https://www.netflix.com/title/80095697 - Disenchantment, Part 1, asked for
    # fewer episodes than it has so the paging can be seen working.
    pytest.param(80117549, 2, id="disenchantment part 1, two episodes"),
    # A movie has no episodes, and is answered with itself rather than refused.
    # https://www.netflix.com/title/81458424
    pytest.param(81458424, None, id="wake up dead man movie"),
]


# TODO: Validate
class PreviewModalEpisodeSelectorSeasonEpisodesTest(RecordedEndpoint):
    MODEL = PreviewModalEpisodeSelectorSeasonEpisodesModel


# TODO: Validate
def recorded_name(season_id: int, count: int | None) -> str:
    """Return the name a season asked for `count` episodes is recorded under."""
    return str(season_id) if count is None else f"{season_id}_{count}"


# TODO: Validate
@pytest.mark.parametrize(("season_id", "count"), SEASONS)
def test_download(client: Meshfilm, season_id: int, count: int | None) -> None:
    endpoint = client.preview_modal_episode_selector_season_episodes
    episode_count = EPISODE_COUNT if count is None else count
    PreviewModalEpisodeSelectorSeasonEpisodesTest.download_test(
        recorded_name(season_id, count),
        lambda: endpoint.download(season_id, episode_count),
    )


# TODO: Validate
@pytest.mark.parametrize(("season_id", "count"), SEASONS)
def test_download_all(client: Meshfilm, season_id: int, count: int | None) -> None:
    endpoint = client.preview_modal_episode_selector_season_episodes
    episode_count = EPISODE_COUNT if count is None else count
    PreviewModalEpisodeSelectorSeasonEpisodesTest.download_test(
        recorded_name(season_id, count),
        # Both pages sizes are the one the season is asked for, so a season
        # recorded with a small count is walked a small page at a time.
        lambda: endpoint.download_all(season_id, episode_count, episode_count),
        "Multipage",
    )


# TODO: Validate
@pytest.mark.parametrize(("season_id", "count"), SEASONS)
def test_parse_all(season_id: int, count: int | None) -> None:
    PreviewModalEpisodeSelectorSeasonEpisodesTest.parse_test(
        recorded_name(season_id, count),
        "Multipage",
    )


# TODO: Validate
@pytest.mark.parametrize(("season_id", "count"), SEASONS)
def test_merge_pages(client: Meshfilm, season_id: int, count: int | None) -> None:
    endpoint = client.preview_modal_episode_selector_season_episodes
    pages = PreviewModalEpisodeSelectorSeasonEpisodesTest.recorded_documents(
        recorded_name(season_id, count),
        "Multipage",
    )
    merged = endpoint.load(endpoint.merge_pages(pages))
    merged_episodes = merged.data.videos[0].episodes
    page_episodes = [
        page.data.videos[0].episodes for page in endpoint.load_pages(pages)
    ]

    if merged_episodes is None:
        # A movie is answered with itself and no episodes, so there is only ever
        # the one page and merging leaves it as it was.
        assert page_episodes == [None]
        return

    assert [edge.node.number for edge in merged_episodes.edges] == [
        edge.node.number
        for episodes in page_episodes
        if episodes is not None
        for edge in episodes.edges
    ]
    assert merged_episodes.page_info.has_next_page is False


# TODO: Validate
@pytest.mark.parametrize(("season_id", "count"), SEASONS)
def test_parse(client: Meshfilm, season_id: int, count: int | None) -> None:
    data = client.preview_modal_episode_selector_season_episodes.load(
        PreviewModalEpisodeSelectorSeasonEpisodesTest.recorded_content(
            recorded_name(season_id, count),
        ),
    )
    assert data.data.videos[0].video_id == season_id


# TODO: Validate
@pytest.mark.parametrize(
    "season_id",
    [pytest.param(1, id="season that does not exist")],
)
def test_download_invalid(client: Meshfilm, season_id: int) -> None:
    PreviewModalEpisodeSelectorSeasonEpisodesTest.error_test(
        season_id,
        lambda: client.preview_modal_episode_selector_season_episodes.download(
            season_id,
        ),
        SeasonNotFoundError,
    )
