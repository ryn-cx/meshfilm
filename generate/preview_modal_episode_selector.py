# TODO: Validate
"""Rebuilds PreviewModalEpisodeSelectorModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, MESHFILM_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from meshfilm import Meshfilm

SHOW_IDS = load_ids("PreviewModalEpisodeSelectorModel")


# TODO: Validate
def generate_preview_modal_episode_selector(client: Meshfilm) -> None:
    """Rebuild PreviewModalEpisodeSelectorModel."""
    endpoint = client.preview_modal_episode_selector
    for show_id in SHOW_IDS:
        download_if_missing(
            FILES_PATH,
            "PreviewModalEpisodeSelectorModel",
            show_id,
            lambda show_id=show_id: endpoint.download(show_id),
        )
    rebuild_model(FILES_PATH, MESHFILM_PATH, "PreviewModalEpisodeSelectorModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_preview_modal_episode_selector(Meshfilm(build_client_automatically()))
