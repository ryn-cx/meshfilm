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
from meshfilm.lodp_title_and_plans_page import extract_video

MODEL_NAME = "LodpTitleAndPlansPageModel"


# TODO: Validate
class Video(RecordingId[Meshfilm]):
    title_id: int

    # TODO: Validate
    def download(self, client: Meshfilm) -> str:
        return client.lodp_title_and_plans_page.download(self.title_id)


TITLE_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, Video)


# TODO: Validate
def generate_lodp_title_and_plans_page(client: Meshfilm) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, TITLE_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, Video, extract_video)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_lodp_title_and_plans_page(Meshfilm(build_client_automatically()))
