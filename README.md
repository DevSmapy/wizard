# WIZARD

**WIZARD** (Weekly Insights on Zealous Art and Release Details) generates a weekly Korean movie release report as Tistory-ready HTML from the KMDB API.

## What it does

1. Fetch release data from KMDB
2. Extract title, date, genre, directors, cast, plot, and poster
3. Render a table of contents + movie cards into one HTML file for manual paste into Tistory

## Setup

1. Clone and enter the repo:
   ```bash
   git clone https://github.com/DevSmapy/wizard.git
   cd wizard
   ```
2. Install dependencies with [uv](https://docs.astral.sh/uv/):
   ```bash
   uv sync
   ```
3. Copy the example config and fill in your KMDB key and release date range:
   ```bash
   cp config.example.json config.json
   ```
4. Run:
   ```bash
   uv run python main.py
   ```

Output path comes from `config.json` (`output_path`). Keep `config.json` local — it is gitignored.
