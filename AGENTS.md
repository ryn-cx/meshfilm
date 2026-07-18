<!-- TODO: Validate -->
# Meshfilm — Netflix's catalog, fully typed

**The Netflix metadata client you didn't know you were missing.** Meshfilm speaks
Netflix's own private GraphQL API and hands you back strongly-typed Python models for
shows, movies, seasons, episodes, and search — no scraping, no guesswork, no untyped
dictionaries to spelunk through.

Point it at a Netflix video ID and get a fully-validated model. There is no step two.

## Why Meshfilm

- **Seven real endpoints, one clean client.** `MeshFilm` exposes the surfaces Netflix's
  own web app uses: `lodp_title_and_plans_page` (a title's details, related titles, and
  plans), `preview_modal_episode_selector` (a show's seasons),
  `preview_modal_episode_selector_season_episodes` (a season's episodes),
  `preview_modal_video_title_group` and `mini_modal` (batch hover-preview data),
  `detail_modal` (a video's detail modal), and `search_page_results` (search). Each one
  is grounded in a persisted GraphQL query the site actually ships.
- **Two names for every endpoint.** Each surface also carries a domain-friendly alias
  that resolves to the same object: `title_page`, `details`, `seasons`, `episodes`,
  `previews`, `mini_previews`, and `search`. Reach for the Netflix operation name when
  you care about the wire, the alias when you care about the domain — both are the same
  endpoint.
- **Typed all the way down.** Every response is a Pydantic model with camelCase Netflix
  fields mapped to Pythonic snake_case — so `client.lodp_title_and_plans_page.get(id)
  .data.videos[0].video_id` is real, autocompleted, and checked.
- **Strict by design.** Models are declared `extra="forbid"`: if Netflix sends a field
  the schema doesn't know about, you hear about it immediately instead of silently
  dropping data. Precision is the whole point.
- **Self-healing schemas.** `parse()` validates against the generated model, and when
  Netflix drifts the shape, it regenerates the model from the new payload and re-parses
  — automatically — so a surprise field is a rebuild, not an outage.
- **Batch in a single call.** `mini_modal` and `preview_modal_video_title_group` take a
  list of IDs and fetch them all in one round trip.
- **Raw or refined, your call.** Every endpoint offers `download()` for the untouched
  GraphQL JSON and `get()` for the parsed model.

## Sixty seconds to your first model

```python
from meshfilm import MeshFilm

client = MeshFilm()

# get() returns a parsed, typed model. download() returns the raw GraphQL JSON.
show = client.lodp_title_and_plans_page.get(80095697)  # Disenchantment
print(show.data.videos[0].video_id)  # -> 80095697

# Batch endpoints take a list of IDs and resolve them in one request.
previews = client.mini_modal.get([80095697, 81458424])

# Need the untouched payload? download() returns the raw GraphQL JSON.
raw = client.detail_modal.download(80095697)
```

## Tested against Netflix itself

The suite doesn't mock — it hits the real API and holds the models to it.

- **Round-trip fidelity.** `TestParse` re-parses *every* captured sample for every
  endpoint on each run, so the strict models are continuously proven against real
  Netflix payloads.
- **Happy path, verified.** `TestGet` fetches live data for shows, movies, seasons,
  episodes, and search, parses it, and confirms the IDs come back exactly as requested.
- **Empty payloads, handled.** Wrong-type IDs, nonexistent IDs, and searches with no
  matches simply parse into a valid, empty model rather than raising — no special-casing
  required at the call site.

## Setup

Meshfilm targets **Python 3.14+**. HTTP is handled by its companion client
[`get-around`](https://github.com/ryn-cx/get-around), and models are generated and kept
honest by [`good-ass-pydantic-integrator`](https://github.com/ryn-cx/good-ass-pydantic-integrator).

Install the project and its dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Then construct a `MeshFilm` client and start calling endpoints. That's it.

---

Unofficial, and not affiliated with Netflix. Built for anyone who wants Netflix's public
title metadata as clean, typed Python — and refuses to settle for a bag of dicts.
