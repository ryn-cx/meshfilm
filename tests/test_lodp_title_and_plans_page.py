from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from meshfilm.exceptions import TitleNotFoundError

if TYPE_CHECKING:
    from meshfilm import Meshfilm

TITLES = [
    pytest.param(80240027, id="Show"),
    pytest.param(82760630, id="Movie"),
]


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLES)
def test_download(client: Meshfilm, title_id: int) -> None:
    lodp_title_and_plans_page = client.lodp_title_and_plans_page(title_id)
    assert lodp_title_and_plans_page.video_id == title_id


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLES)
def test_similar_videos(client: Meshfilm, title_id: int) -> None:
    lodp_title_and_plans_page = client.lodp_title_and_plans_page(title_id)
    assert lodp_title_and_plans_page.similar_videos


# TODO: Validate
def test_download_invalid(client: Meshfilm) -> None:
    with pytest.raises(TitleNotFoundError):
        client.lodp_title_and_plans_page.download(1)
