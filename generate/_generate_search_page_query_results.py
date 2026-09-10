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
from meshfilm.search_page_query_results import extract_results

MODEL_NAME = "SearchPageQueryResultsModel"


class Search(RecordingId[Meshfilm]):
    search_term: str

    def download(self, client: Meshfilm) -> str:
        return client.search_page_query_results.download(self.search_term)


SEARCH_TERMS = load_ids(GENERATOR_PATHS, MODEL_NAME, Search)


def generate_search_page_query_results(client: Meshfilm) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SEARCH_TERMS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, Search, extract_results)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_page_query_results(Meshfilm(build_client_automatically()))
