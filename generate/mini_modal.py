# TODO: Validate
"""Rebuilds MiniModalModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, MESHFILM_PATH
from generate.utils import download_if_missing
from meshfilm import Meshfilm

VIDEO_ID_BATCHES = [(80095697, 81458424), (80095697, 1)]
"""The endpoint is asked about a batch of titles at a time."""


# TODO: Validate
def generate_mini_modal(client: Meshfilm) -> None:
    """Rebuild MiniModalModel."""
    for video_ids in VIDEO_ID_BATCHES:
        download_if_missing(
            FILES_PATH,
            "MiniModalModel",
            "_".join(str(video_id) for video_id in video_ids),
            lambda video_ids=video_ids: client.mini_modal.download(video_ids),
        )
    generate_model(FILES_PATH, MESHFILM_PATH, "MiniModalModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_mini_modal(Meshfilm(build_client_automatically()))
