# Self-hosted Firecrawl — local setup notes

The vault's scrape scripts (`scripts/scrape_with_firecrawl.py` and friends)
hit a self-hosted Firecrawl on `http://localhost:3002`. These notes capture
how the local stack is wired so you (or a future agent) can re-create it.

## Where it lives

- Repo:  `~/Documents/GitHub/firecrawl` (clone of `mendableai/firecrawl`)
- Compose stack: `~/Documents/GitHub/firecrawl/docker-compose.yaml`
  + local override: `~/Documents/GitHub/firecrawl/docker-compose.override.yaml`
- Local config: `~/Documents/GitHub/firecrawl/.env`

## Override vs upstream

We use an `override.yaml` (not upstream edits) so `git pull` in the firecrawl
repo never conflicts. The override does two things:

1. Switches `api`, `playwright-service`, and `nuq-postgres` from `build:` to
   prebuilt `ghcr.io/firecrawl/*:latest` images. First-time bring-up takes
   minutes instead of half an hour.
2. Lowers `mem_limit` / `cpus` to fit in a 7.6 GB Docker Desktop allocation
   (api: 3 GB / 2 CPU, playwright: 2 GB / 1.5 CPU). Upstream defaults total
   ~12 GB which OOMs this host.
3. Extends rabbitmq's healthcheck `start_period` to 60s — the upstream 5s
   window is too tight for cold start on this host and causes the api
   container to fail its dependency check.

## Postgres credentials gotcha

The upstream `.env.example` template *suggests* `POSTGRES_DB=firecrawl` /
`POSTGRES_USER=firecrawl`. **Do not use that.** The nuq-postgres init
script tries to create the `pg_cron` extension, and `pg_cron` requires the
database name to match `cron.database_name` in `postgresql.conf` —
hardcoded to `postgres` in this image. Setting `POSTGRES_DB=firecrawl`
breaks first-time init and the api crashes with
`relation "nuq.queue_crawl_finished" does not exist`.

Stick with the defaults:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```

If you ever change these and need to undo, you must wipe the volume:

```bash
cd ~/Documents/GitHub/firecrawl
docker compose down --volumes   # destroys postgres data so init runs again
docker compose up -d
```

## Bringing the stack up

```bash
cd ~/Documents/GitHub/firecrawl
docker compose up -d
```

Wait ~60s for warm-up. Confirm the api is listening:

```bash
curl -sf http://localhost:3002/v1/scrape \
  -X POST -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}' | head -c 200
```

Should return `{"success":true,"data":{"markdown":"Example Domain..."}}`.

## Bringing it down

```bash
cd ~/Documents/GitHub/firecrawl
docker compose down            # stop, keep data volume
docker compose down --volumes  # stop and wipe data volume
```

## Resource tuning

The scrape scripts open up to `MAX_WORKERS=5` parallel requests against
`/v1/scrape`. The matching server-side knobs (in `.env`) are:

- `MAX_CONCURRENT_JOBS=3`     — total concurrent scrape jobs the worker pool serves
- `BROWSER_POOL_SIZE=3`       — Playwright browser instances kept warm
- `CRAWL_CONCURRENT_REQUESTS=5` — per-crawl request fanout
- `NUM_WORKERS_PER_QUEUE=4`   — queue worker count

If Activity Monitor shows headroom and you want faster bulk crawls, raise
these and bounce the api container:

```bash
docker compose restart api
```

## What lives in this directory

Everything else under `.firecrawl/` (the `*-all-urls.txt`, `*-status.json`,
`*-crawl.json`, `*.log` files) is **output** from past crawl runs. The
scrape scripts in `scripts/` write here.
