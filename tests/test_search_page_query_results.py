from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from meshfilm import Meshfilm

SEARCH_TERMS = [
    pytest.param("Disenchantment", id="Show"),
    pytest.param("Teenage Wastelane", id="Movie"),
]


@pytest.mark.parametrize("search_term", SEARCH_TERMS)
def test_download(client: Meshfilm, search_term: str) -> None:
    search_page_query_results = client.search_page_query_results(search_term)
    assert search_page_query_results.data.page.sections.edges


def test_download_invalid(client: Meshfilm) -> None:
    search_page_query_results = client.search_page_query_results(
        "123456 qwert asdfg zxcvb",
    )
    assert not search_page_query_results.data.page.sections.edges
