# TODO: Validate
from __future__ import annotations

import json
from pathlib import Path

import pytest
from get_around import build_client_automatically

from meshfilm import Meshfilm
from meshfilm.exceptions import NoContentError

ENV_FILE = Path(__file__).parent.parent / ".env"

client = Meshfilm(build_client_automatically())

SHOW_NAME = "Disenchantment"
"""A search term that matches a title."""
SHOW_ID = 80095697
"""show_id of Disenchantment."""
SEASON_1_ID = 80117549
"""season_id of Disenchantment Season 1."""
SEASON_2_ID = 80174140
"""season_id of Disenchantment Season 2."""
EPISODE_ID = 80117711
"""episode_id of Disenchantment Season 1 Episode 1."""
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
INVALID_SHOW_NAME = "qwertasdfgzxcvb"


class TestAliases:
    @pytest.mark.parametrize(
        ("alias", "operation"),
        [
            ("title_page", "lodp_title_and_plans_page"),
            ("details", "detail_modal"),
            ("seasons", "preview_modal_episode_selector"),
            ("episodes", "preview_modal_episode_selector_season_episodes"),
            ("previews", "preview_modal_video_title_group"),
            ("mini_previews", "mini_modal"),
            ("search", "search_page_results"),
        ],
    )
    def test_alias_is_operation(self, alias: str, operation: str) -> None:
        assert getattr(client, alias) is getattr(client, operation)


class TestGet:
    @pytest.mark.parametrize(
        "video_id",
        [SHOW_ID, EPISODE_ID, MOVIE_ID],
        ids=[f"{SHOW_ID=}", f"{EPISODE_ID=}", f"{MOVIE_ID=}"],
    )
    def test_get_lodp_title_and_plans_page(self, video_id: int) -> None:
        endpoint = client.lodp_title_and_plans_page
        model = endpoint.get(video_id)
        assert any(video.video_id == video_id for video in model.data.videos)
        endpoint.save_new_json_file(endpoint.original_input(model))

    @pytest.mark.parametrize(
        "season_id",
        [SEASON_1_ID, SEASON_2_ID],
        ids=[f"{SEASON_1_ID=}", f"{SEASON_2_ID=}"],
    )
    def test_get_preview_modal_episode_selector_season_episodes(
        self,
        season_id: int,
    ) -> None:
        endpoint = client.preview_modal_episode_selector_season_episodes
        model = endpoint.get(season_id)
        assert any(
            video.video_id == season_id and video.field__typename == "Season"
            for video in model.data.videos
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_preview_modal_episode_selector(self) -> None:
        endpoint = client.preview_modal_episode_selector
        model = endpoint.get(SHOW_ID)
        assert any(video.video_id == SHOW_ID for video in model.data.videos)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_search_page_results(self) -> None:
        endpoint = client.search_page_results
        model = endpoint.get(SHOW_NAME)
        titles = [
            entity.node.display_string
            for section in model.data.page.sections.edges
            for entity in section.node.entities.edges
        ]
        assert any(SHOW_NAME in title for title in titles)
        endpoint.save_new_json_file(endpoint.original_input(model))

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
    def test_get_mini_modal(self, video_ids: list[str | int]) -> None:
        endpoint = client.mini_modal
        model = endpoint.get(video_ids)
        returned_ids = {entity.video_id for entity in model.data.unified_entities}
        assert all(int(video_id) in returned_ids for video_id in video_ids)
        endpoint.save_new_json_file(endpoint.original_input(model))

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
    def test_get_detail_modal(self, video_id: int) -> None:
        endpoint = client.detail_modal
        model = endpoint.get(video_id)
        assert any(
            entity.video_id == video_id for entity in model.data.unified_entities
        )
        endpoint.save_new_json_file(endpoint.original_input(model))

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
    def test_get_preview_modal_video_title_group(
        self,
        video_ids: list[str | int],
    ) -> None:
        endpoint = client.preview_modal_video_title_group
        model = endpoint.get(video_ids)
        returned_ids = {video.video_id for video in model.data.videos}
        assert all(int(video_id) in returned_ids for video_id in video_ids)
        endpoint.save_new_json_file(endpoint.original_input(model))


class TestInvalidGet:
    @pytest.mark.parametrize(
        "invalid_id",
        [SEASON_1_ID, SEASON_2_ID, INVALID_ID],
        ids=[f"{SEASON_1_ID=}", f"{SEASON_2_ID=}", f"{INVALID_ID=}"],
    )
    def test_invalid_get_lodp_title_and_plans_page(
        self,
        invalid_id: int,
    ) -> None:
        with pytest.raises(NoContentError) as error:
            client.lodp_title_and_plans_page.get(invalid_id)

        assert error.value.response

    @pytest.mark.parametrize(
        "invalid_id",
        [SHOW_ID, EPISODE_ID, MOVIE_ID, INVALID_ID],
        ids=[f"{SHOW_ID=}", f"{EPISODE_ID=}", f"{MOVIE_ID=}", f"{INVALID_ID=}"],
    )
    def test_invalid_get_preview_modal_episode_selector_season_episodes(
        self,
        invalid_id: int,
    ) -> None:
        with pytest.raises(NoContentError) as error:
            client.preview_modal_episode_selector_season_episodes.get(invalid_id)
        assert "data" in error.value.response

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
    def test_invalid_get_preview_modal_episode_selector(
        self,
        invalid_id: int,
    ) -> None:
        with pytest.raises(NoContentError) as error:
            client.preview_modal_episode_selector.get(invalid_id)
        assert "data" in error.value.response

    def test_invalid_get_mini_modal(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.mini_modal.get([INVALID_ID])
        assert "data" in error.value.response

    def test_invalid_get_preview_modal_video_title_group(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.preview_modal_video_title_group.get([INVALID_ID])
        assert "data" in error.value.response

    def test_invalid_get_detail_modal(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.detail_modal.get(INVALID_ID)
        assert "data" in error.value.response

    def test_invalid_get_search_page_results(self) -> None:
        with pytest.raises(NoContentError) as error:
            client.search_page_results.get(INVALID_SHOW_NAME)
        assert "data" in error.value.response


class TestParse:
    @pytest.mark.parametrize(
        "endpoint_name",
        [
            "lodp_title_and_plans_page",
            "preview_modal_episode_selector_season_episodes",
            "preview_modal_episode_selector",
            "search_page_results",
            "mini_modal",
            "detail_modal",
            "preview_modal_video_title_group",
        ],
    )
    def test_parse(self, endpoint_name: str) -> None:
        endpoint = getattr(client, endpoint_name)
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
