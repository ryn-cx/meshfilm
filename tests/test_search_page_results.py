# TODO: Validate
import json

import pytest
from get_around import build_client_automatically

from meshfilm import Meshfilm
from meshfilm.exceptions import NoContentError

client = Meshfilm(build_client_automatically())

SHOW_NAME = "Disenchantment"
"""A search term that matches a title."""
INVALID_SHOW_NAME = "qwertasdfgzxcvb"


class TestSearchPageResults:
    def test_alias(self) -> None:
        assert client.search is client.search_page_results

    def test_get(self) -> None:
        endpoint = client.search_page_results
        model = endpoint.get(SHOW_NAME)
        titles = [
            entity.node.display_string
            for section in model.data.page.sections.edges
            for entity in section.node.entities.edges
        ]
        assert any(SHOW_NAME in title for title in titles)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.search_page_results.get(INVALID_SHOW_NAME)
        assert "data" in error.value.response

    def test_parse(self) -> None:
        endpoint = client.search_page_results
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
