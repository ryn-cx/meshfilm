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
from meshfilm import Meshfilm

client = Meshfilm()

# Available endpoints
title_page = client.title_page.get(80095697)
seasons = client.seasons.get(80095697)
episodes = client.episodes.get(80117549)
previews = client.previews.get([80095697, 81458424])
results = client.search.get("Disenchantment")
```

Endpoints can also be accessed using Netflix's oprartionName.

| Meshfilm Alias | Netflix oprartionName |
| --- | --- |
| `title_page` | `lodp_title_and_plans_page` |
| `details` | `detail_modal` |
| `seasons` | `preview_modal_episode_selector` |
| `episodes` | `preview_modal_episode_selector_season_episodes` |
| `previews` | `preview_modal_video_title_group` |
| `mini_previews` | `mini_modal` |
| `search` | `search_page_results` |
