# Meshfilm

Netflix API wrapper built using [Good Ass Pydantic
Integrator](https://github.com/ryn-cx/good-ass-pydantic-integrator) and [Get
Around](https://github.com/ryn-cx/get-around).

## Install

Requires Python 3.14+. Install with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Usage

Every endpoint has `get()` (parsed, typed model) and `download()` (raw GraphQL JSON).

```python
from meshfilm import MeshFilm

client = MeshFilm()

# Available endpoints
lodp_title_and_plans_page = client.lodp_title_and_plans_page.get(80095697)  # Disenchantment
detail_modal = client.detail_modal.get(80095697)
preview_modal_episode_selector = client.preview_modal_episode_selector.get(80095697)
preview_modal_episode_selector_season_episodes = client.preview_modal_episode_selector_season_episodes.get(80117549)
mini_modal = client.mini_modal.get([80095697, 81458424])
preview_modal_video_title_group = client.preview_modal_video_title_group.get([80095697, 81458424])
search_page_results = client.search_page_results.get("Disenchantment")
```
