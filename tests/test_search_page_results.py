# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from meshfilm import Meshfilm
    from meshfilm.search_page_results import SearchPageResults

SHOW_NAME = "Disenchantment"
"""A search term that matches a title."""


@pytest.fixture(scope="session")
def endpoint(client: Meshfilm) -> SearchPageResults:
    return client.search_page_results


class TestSearchPageResults:
    def test_alias(self, client: Meshfilm) -> None:
        assert client.search is client.search_page_results

    def test_download(self, endpoint: SearchPageResults) -> None:
        download_and_save(
            endpoint,
            SHOW_NAME,
            lambda: endpoint.download(SHOW_NAME),
        )

    def test_parse(self, endpoint: SearchPageResults) -> None:
        parsed_json(endpoint, SHOW_NAME)
        # TODO: assert expected value (needs live data)
