# TODO: Validate
"""Rebuilds PreviewModalEpisodeSelectorSeasonEpisodesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, MESHFILM_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from meshfilm import Meshfilm
from meshfilm.preview_modal_episode_selector_season_episodes import EPISODE_COUNT

MODEL_NAME = "PreviewModalEpisodeSelectorSeasonEpisodesModel"

SEASONS = load_ids("PreviewModalEpisodeSelectorSeasonEpisodesModel")
"""Each season and how many episodes it was asked for, None for the default."""


# TODO: Validate
def generate_preview_modal_episode_selector_season_episodes(
    client: Meshfilm,
) -> None:
    """Rebuild PreviewModalEpisodeSelectorSeasonEpisodesModel."""
    endpoint = client.preview_modal_episode_selector_season_episodes
    for season_id, count in SEASONS:
        download_if_missing(
            FILES_PATH,
            MODEL_NAME,
            str(season_id) if count is None else f"{season_id}_{count}",
            lambda season_id=season_id, count=count: endpoint.download(
                season_id,
                EPISODE_COUNT if count is None else count,
            ),
        )
    rebuild_model(
        FILES_PATH,
        MESHFILM_PATH,
        MODEL_NAME,
        name_of=lambda season: (
            str(season[0]) if season[1] is None else f"{season[0]}_{season[1]}"
        ),
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_preview_modal_episode_selector_season_episodes(
        Meshfilm(build_client_automatically()),
    )
