# TODO: Validate
import json

import pytest
from get_around import build_client_automatically

from meshfilm import Meshfilm
from meshfilm.exceptions import NoContentError

client = Meshfilm(build_client_automatically())

SHOW_ID = 80095697
"""show_id of Disenchantment."""
SEASON_1_ID = 80117549
"""season_id of Disenchantment Season 1."""
SEASON_2_ID = 80174140
"""season_id of Disenchantment Season 2."""
EPISODE_ID = 80117711
"""episode_id of Disenchantment Season 1 Episode 1."""
INVALID_ID = 1
MOVIE_ID = 81458424
""""movie_id of Watch Wake Up Dead Man: A Knives Out Mystery."""


class TestDetailModal:
    def test_alias(self) -> None:
        assert client.details is client.detail_modal

    @pytest.mark.parametrize(
        "video_id",
        [EPISODE_ID, SHOW_ID, SEASON_1_ID, SEASON_2_ID, MOVIE_ID],
        ids=[
            f"{EPISODE_ID=}",
            f"{SHOW_ID=}",
            f"{SEASON_1_ID=}",
            f"{SEASON_2_ID=}",
            f"{MOVIE_ID=}",
        ],
    )
    def test_get(self, video_id: int) -> None:
        endpoint = client.detail_modal
        model = endpoint.get(video_id)
        assert any(
            entity.video_id == video_id for entity in model.data.unified_entities
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.detail_modal.get(INVALID_ID)
        assert "data" in error.value.response

    def test_parse(self) -> None:
        endpoint = client.detail_modal
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
