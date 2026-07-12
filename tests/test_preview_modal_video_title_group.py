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
INVALID_ID = 1
SEASON_1_EPISODE_IDS: list[str | int] = [
    80117711,
    80145115,
    80145117,
    80145118,
    80145119,
    80145116,
    80145120,
    80145121,
    80145122,
    80145123,
]
"""Every episode from Disenchantment's first season."""
MOVIE_ID = 81458424
""""movie_id of Watch Wake Up Dead Man: A Knives Out Mystery."""


class TestPreviewModalVideoTitleGroup:
    def test_alias(self) -> None:
        assert client.previews is client.preview_modal_video_title_group

    @pytest.mark.parametrize(
        "video_ids",
        [[SHOW_ID], [SEASON_1_ID], [SEASON_2_ID], [MOVIE_ID], SEASON_1_EPISODE_IDS],
        ids=[
            f"{SHOW_ID=}",
            f"{SEASON_1_ID=}",
            f"{SEASON_2_ID=}",
            f"{MOVIE_ID=}",
            f"{SEASON_1_EPISODE_IDS=}",
        ],
    )
    def test_get(self, video_ids: list[str | int]) -> None:
        endpoint = client.preview_modal_video_title_group
        model = endpoint.get(video_ids)
        returned_ids = {video.video_id for video in model.data.videos}
        assert all(int(video_id) in returned_ids for video_id in video_ids)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_invalid_get(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.preview_modal_video_title_group.get([INVALID_ID])
        assert "data" in error.value.response

    def test_parse(self) -> None:
        endpoint = client.preview_modal_video_title_group
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
