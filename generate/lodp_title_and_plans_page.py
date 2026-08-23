# TODO: Validate
"""Rebuilds LodpTitleAndPlansPageModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, MESHFILM_PATH
from generate.utils import download_if_missing
from meshfilm import Meshfilm

VIDEO_IDS = [80095697, 81458424]


# TODO: Validate
def generate_lodp_title_and_plans_page(client: Meshfilm) -> None:
    """Rebuild LodpTitleAndPlansPageModel."""
    endpoint = client.lodp_title_and_plans_page
    for video_id in VIDEO_IDS:
        download_if_missing(
            FILES_PATH,
            "LodpTitleAndPlansPageModel",
            video_id,
            lambda video_id=video_id: endpoint.download(video_id),
        )
    generate_model(FILES_PATH, MESHFILM_PATH, "LodpTitleAndPlansPageModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_lodp_title_and_plans_page(Meshfilm(build_client_automatically()))
