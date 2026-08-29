# TODO: Validate
"""Rebuilds DetailModalModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, MESHFILM_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from meshfilm import Meshfilm

VIDEO_IDS = load_ids("DetailModalModel")


# TODO: Validate
def generate_detail_modal(client: Meshfilm) -> None:
    """Rebuild DetailModalModel."""
    for video_id in VIDEO_IDS:
        download_if_missing(
            FILES_PATH,
            "DetailModalModel",
            video_id,
            lambda video_id=video_id: client.detail_modal.download(video_id),
        )
    rebuild_model(FILES_PATH, MESHFILM_PATH, "DetailModalModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail_modal(Meshfilm(build_client_automatically()))
