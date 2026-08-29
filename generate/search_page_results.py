# TODO: Validate
"""Rebuilds SearchPageResultsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, MESHFILM_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from meshfilm import Meshfilm

SEARCH_TERMS = load_ids("SearchPageResultsModel")


# TODO: Validate
def generate_search_page_results(client: Meshfilm) -> None:
    """Rebuild SearchPageResultsModel."""
    for search_term in SEARCH_TERMS:
        download_if_missing(
            FILES_PATH,
            "SearchPageResultsModel",
            search_term,
            lambda search_term=search_term: client.search_page_results.download(
                search_term,
            ),
        )
    rebuild_model(FILES_PATH, MESHFILM_PATH, "SearchPageResultsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_page_results(Meshfilm(build_client_automatically()))
