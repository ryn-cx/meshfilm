# TODO: Validate
"""Rebuilds PreviewModalVideoTitleGroupModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, MESHFILM_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from meshfilm import Meshfilm

VIDEO_ID_BATCHES = load_ids("PreviewModalVideoTitleGroupModel")
"""The endpoint is asked about a batch of titles at a time."""


# TODO: Validate
def generate_preview_modal_video_title_group(client: Meshfilm) -> None:
    """Rebuild PreviewModalVideoTitleGroupModel."""
    endpoint = client.preview_modal_video_title_group
    for video_ids in VIDEO_ID_BATCHES:
        download_if_missing(
            FILES_PATH,
            "PreviewModalVideoTitleGroupModel",
            "_".join(str(video_id) for video_id in video_ids),
            lambda video_ids=video_ids: endpoint.download(video_ids),
        )
    rebuild_model(
        FILES_PATH,
        MESHFILM_PATH,
        "PreviewModalVideoTitleGroupModel",
        name_of=lambda batch: "_".join(str(video_id) for video_id in batch),
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_preview_modal_video_title_group(Meshfilm(build_client_automatically()))
