# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.search_page_results.models import SearchPageResultsModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from meshfilm import Meshfilm

SEARCH_TERMS = [
    pytest.param("Disenchantment", id="a term with an exact match"),
    # Netflix never answers a search with nothing: a term it matches badly is
    # answered with whatever it matches at all.
    pytest.param("zzzzqqqxxnomatch", id="a term with no exact match"),
]


# TODO: Validate
class SearchPageResultsTest(RecordedEndpoint):
    MODEL = SearchPageResultsModel


# TODO: Validate
@pytest.mark.parametrize("search_term", SEARCH_TERMS)
def test_download(client: Meshfilm, search_term: str) -> None:
    SearchPageResultsTest.download_test(
        search_term,
        lambda: client.search_page_results.download(search_term),
    )


# TODO: Validate
@pytest.mark.parametrize("search_term", SEARCH_TERMS)
def test_parse(client: Meshfilm, search_term: str) -> None:
    data = client.search_page_results.load(
        SearchPageResultsTest.recorded_content(search_term),
    )
    assert data.data.page.sections.edges
