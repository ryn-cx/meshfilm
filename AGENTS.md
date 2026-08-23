<!-- TODO: Validate -->
# Meshfilm — Netflix's catalog

Meshfilm speaks Netflix's own private GraphQL API and hands back Pydantic models
generated from the responses recorded under `generate/_files`.

## How it is put together

- **Seven endpoints, one client.** `Meshfilm` exposes the surfaces Netflix's own
  web app uses: `lodp_title_and_plans_page` (a title's page and the plans on
  offer), `preview_modal_episode_selector` (a show's seasons),
  `preview_modal_episode_selector_season_episodes` (a season's episodes),
  `preview_modal_video_title_group` and `mini_modal` (batch hover-preview data),
  `detail_modal` (a title's detail modal), and `search_page_results` (search).
  Each one sends a persisted query the site itself ships.
- **Two names for every endpoint.** Each surface also carries a domain-friendly
  alias that resolves to the same object: `title_page`, `details`, `seasons`,
  `episodes`, `previews`, `mini_previews`, and `search`.
- **Three methods per endpoint.** `download()` returns the response as text,
  `load()` reads text into the model, and calling the endpoint does both.
- **Models are generated.** `models.json`, `strict_models.py`,
  `optional_models.py` and `models.py` are written by
  `generate/generate_models.py` from the recorded responses and are never edited
  by hand. A type checker reads the strict model and the running program reads
  the all-optional one, so a response that has drifted still parses.
- **Not found is checked in the body.** Netflix answers an unknown id with a 200
  and a null where the title would be, so each endpoint raises its own
  `NotFoundError` for that rather than relying on the status code.

## Sixty seconds in

```python
from meshfilm import Meshfilm

client = Meshfilm()

details = client.detail_modal(80095697)  # Disenchantment
print(details.data.unified_entities[0].title)

previews = client.mini_modal([80095697, 81458424])  # one request, two titles
downloaded = client.detail_modal.download(80095697)  # the response as text
```

## Tests

The suite does not mock. `test_download` hits the real API when a recording is
missing or a week old and skips otherwise, so recordings under `tests/_files/`
are read from disk most of the time. `test_parse` reads a recording back through
the endpoint's `load`. `test_download_invalid` records what the API answers for
an id nothing is under, under `tests/_files/Errors/`.

The models are built from a second copy of the recordings under `generate/_files`.
Regenerate them after adding a recording:

```bash
uv run python -m generate.generate_models
```

## Setup

Meshfilm targets **Python 3.14+**. HTTP is handled by its companion client
[`get-around`](https://github.com/ryn-cx/get-around).

```bash
uv sync
```

---

Unofficial, and not affiliated with Netflix.
