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


class TestLodpTitleAndPlansPage:
    def test_alias(self) -> None:
        assert client.title_page is client.lodp_title_and_plans_page

    @pytest.mark.parametrize(
        "video_id",
        [SHOW_ID, EPISODE_ID, MOVIE_ID],
        ids=[f"{SHOW_ID=}", f"{EPISODE_ID=}", f"{MOVIE_ID=}"],
    )
    def test_get(self, video_id: int) -> None:
        endpoint = client.lodp_title_and_plans_page
        model = endpoint.get(video_id)
        assert any(video.video_id == video_id for video in model.data.videos)
        endpoint.save_new_json_file(endpoint.original_input(model))

    @pytest.mark.parametrize(
        "invalid_id",
        [SEASON_1_ID, SEASON_2_ID, INVALID_ID],
        ids=[f"{SEASON_1_ID=}", f"{SEASON_2_ID=}", f"{INVALID_ID=}"],
    )
    def test_invalid_get(self, invalid_id: int) -> None:
        with pytest.raises(NoContentError) as error:
            client.lodp_title_and_plans_page.get(invalid_id)

        assert error.value.response

    def test_parse(self) -> None:
        endpoint = client.lodp_title_and_plans_page
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
