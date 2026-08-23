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
