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


class TestPreviewModalEpisodeSelector:
    def test_alias(self) -> None:
        assert client.seasons is client.preview_modal_episode_selector

    def test_get(self) -> None:
        endpoint = client.preview_modal_episode_selector
        model = endpoint.get(SHOW_ID)
        assert any(video.video_id == SHOW_ID for video in model.data.videos)
        endpoint.save_new_json_file(endpoint.original_input(model))

    @pytest.mark.parametrize(
        "invalid_id",
        [SEASON_1_ID, SEASON_2_ID, EPISODE_ID, MOVIE_ID, INVALID_ID],
        ids=[
            f"{SEASON_1_ID=}",
            f"{SEASON_2_ID=}",
            f"{EPISODE_ID=}",
            f"{MOVIE_ID=}",
            f"{INVALID_ID=}",
        ],
    )
    def test_invalid_get(self, invalid_id: int) -> None:
        with pytest.raises(NoContentError) as error:
            client.preview_modal_episode_selector.get(invalid_id)
        assert "data" in error.value.response

    def test_parse(self) -> None:
        endpoint = client.preview_modal_episode_selector
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
