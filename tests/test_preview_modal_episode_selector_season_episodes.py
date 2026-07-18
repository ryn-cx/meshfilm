# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from meshfilm import Meshfilm
    from meshfilm.preview_modal_episode_selector_season_episodes import (
        PreviewModalEpisodeSelectorSeasonEpisodes,
    )

SEASON_1_ID = 80117549
"""season_id of Disenchantment Season 1."""
SEASON_2_ID = 80174140
"""season_id of Disenchantment Season 2."""

SEASON_IDS = [SEASON_1_ID, SEASON_2_ID]


@pytest.fixture(scope="session")
def endpoint(client: Meshfilm) -> PreviewModalEpisodeSelectorSeasonEpisodes:
    return client.preview_modal_episode_selector_season_episodes


class TestPreviewModalEpisodeSelectorSeasonEpisodes:
    def test_alias(self, client: Meshfilm) -> None:
        assert client.episodes is client.preview_modal_episode_selector_season_episodes

    @pytest.mark.parametrize("season_id", SEASON_IDS)
    def test_download(
        self,
        endpoint: PreviewModalEpisodeSelectorSeasonEpisodes,
        season_id: int,
    ) -> None:
        download_and_save(
            endpoint,
            str(season_id),
            lambda: endpoint.download(season_id),
        )

    @pytest.mark.parametrize("season_id", SEASON_IDS)
    def test_parse(
        self,
        endpoint: PreviewModalEpisodeSelectorSeasonEpisodes,
        season_id: int,
    ) -> None:
        parse_json(endpoint, str(season_id))
        # TODO: assert expected value (needs live data)


@pytest.mark.parametrize("count", [None, 10])
def test_log_id(
    endpoint: PreviewModalEpisodeSelectorSeasonEpisodes,
    count: int | None,
) -> None:
    kwargs = {} if count is None else {"count": count}
    expected = f"PreviewModalEpisodeSelectorSeasonEpisodes season_id={SEASON_1_ID!r}"
    if count is not None:
        expected += f" count={count!r}"
    assert endpoint.get_log_id(SEASON_1_ID, **kwargs) == expected
