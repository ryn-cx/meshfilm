<!-- TODO: Validate -->
# Meshfilm

[Netflix](https://www.netflix.com) API wrapper built using [Good Ass Pydantic
Integrator](https://github.com/ryn-cx/good-ass-pydantic-integrator) and [Get
Around](https://github.com/ryn-cx/get-around).

## Install

Requires Python 3.14+. Install with [uv](https://docs.astral.sh/uv/):

```bash
uv add git+https://github.com/ryn-cx/meshfilm
```

## Usage

Every endpoint is called to get the parsed model, and `download()` and `load()`
are the two halves of that.

```python
from meshfilm import Meshfilm

client = Meshfilm()

details = client.detail_modal(80095697)
title_page = client.lodp_title_and_plans_page(80095697)
seasons = client.preview_modal_episode_selector(80095697)
episodes = client.preview_modal_episode_selector_season_episodes(80117549)
previews = client.preview_modal_video_title_group([80095697, 81458424])
results = client.search_page_results("Disenchantment")

downloaded = client.detail_modal.download(80095697)  # the response as text
details = client.detail_modal.load(downloaded)
```

Every endpoint is named after the operation Netflix sends it as, and is also
reachable under a name that says what it answers with.

| Alias | Netflix operationName |
| --- | --- |
| `title_page` | `lodp_title_and_plans_page` |
| `details` | `detail_modal` |
| `seasons` | `preview_modal_episode_selector` |
| `episodes` | `preview_modal_episode_selector_season_episodes` |
| `previews` | `preview_modal_video_title_group` |
| `mini_previews` | `mini_modal` |
| `search` | `search_page_results` |
