# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from get_around import build_client_automatically

from meshfilm import Meshfilm
from tests.utils import (
    assert_no_content_error,
    data_path,
    download_if_missing,
)

if TYPE_CHECKING:
    from meshfilm.search_page_results import SearchPageResults

client = Meshfilm(build_client_automatically())

SHOW_NAME = "Disenchantment"
"""A search term that matches a title."""
INVALID_SHOW_NAME = "qwertasdfgzxcvb"


@pytest.fixture(scope="session")
def endpoint() -> SearchPageResults:
    return client.search_page_results


class TestSearchPageResults:
    def test_alias(self) -> None:
        assert client.search is client.search_page_results

    def test_download(self, endpoint: SearchPageResults) -> None:
        download_if_missing(
            endpoint,
            SHOW_NAME,
            lambda: endpoint.download(SHOW_NAME),
        )

    def test_value(self, endpoint: SearchPageResults) -> None:
        endpoint.parse(json.loads(data_path(endpoint, SHOW_NAME).read_text()))
        # TODO: assert expected value (needs live data)

    def test_invalid(self, endpoint: SearchPageResults) -> None:
        name = INVALID_SHOW_NAME
        assert_no_content_error(endpoint, name, lambda: endpoint.get(INVALID_SHOW_NAME))
