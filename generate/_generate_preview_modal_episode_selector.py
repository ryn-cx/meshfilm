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
from meshfilm.preview_modal_episode_selector import extract_show

MODEL_NAME = "PreviewModalEpisodeSelectorModel"


class Show(RecordingId[Meshfilm]):
    show_id: int
    season_count: int | None = None

    def download(self, client: Meshfilm) -> str:
        return client.preview_modal_episode_selector.download(
            self.show_id,
            self.season_count,
        )


SHOW_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, Show)


def generate_preview_modal_episode_selector(client: Meshfilm) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SHOW_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, Show, extract_show)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_preview_modal_episode_selector(Meshfilm(build_client_automatically()))
