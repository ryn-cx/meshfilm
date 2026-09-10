from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from meshfilm import Meshfilm
from meshfilm.preview_modal_episode_selector_season_episodes import extract_season

MODEL_NAME = "PreviewModalEpisodeSelectorSeasonEpisodesModel"


class Season(RecordingId[Meshfilm]):
    season_id: int

    def download(self, client: Meshfilm) -> str:
        endpoint = client.preview_modal_episode_selector_season_episodes
        return endpoint.download(self.season_id)


SEASON_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, Season)


def generate_preview_modal_episode_selector_season_episodes(
    client: Meshfilm,
) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SEASON_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, Season, extract_season)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    client = Meshfilm(build_client_automatically())
    generate_preview_modal_episode_selector_season_episodes(client)
