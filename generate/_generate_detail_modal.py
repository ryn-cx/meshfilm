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

MODEL_NAME = "DetailModalModel"


# TODO: Validate
class Video(RecordingId[Meshfilm]):
    title_id: int

    # TODO: Validate
    def download(self, client: Meshfilm) -> str:
        return client.detail_modal.download(self.title_id)


TITLE_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, Video)


def generate_detail_modal(client: Meshfilm) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, TITLE_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, Video)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail_modal(Meshfilm(build_client_automatically()))
