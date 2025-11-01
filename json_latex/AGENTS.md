# Repository Guidelines

## Project Structure & Module Organization
- `main.py` loads section builders from `templates/` and orchestrates converting JSON data into LaTeX fragments before compiling PDFs with `xelatex`.
- `templates/*.py` each render a resume section into `resume/*.tex`; keep related assets alongside their template for clarity.
- `resume/` holds generated section files plus language-specific `resume_<lang>.tex` entry points; do not edit these by hand unless you are verifying output.
- `awesome-cv.cls` provides the base LaTeX class and should remain untouched unless you are tracking upstream changes.
- Configuration comes from `.env` (see below) and JSON data directories pointed to by `JSON_PATH`.

## Build, Test, and Development Commands
- Install the Python environment (3.13) with `uv sync` or `python -m venv .venv && .venv/bin/pip install python-dotenv`.
- Create a `.env` containing `JSON_PATH=/absolute/path/to/json/` so the loaders can locate your data.
- Regenerate both language variants with:
```bash
uv run python main.py
```
  which copies `resume.tex` to `resume_en.tex` / `resume_it.tex`, refreshes section files, and invokes `xelatex`.
- Re-run `xelatex resume_en.tex` (or the Italian variant) if you tweak LaTeX manually to validate the document without regenerating JSON.

## Coding Style & Naming Conventions
- Follow four-space indentation, `snake_case` functions, and descriptive module names matching the section they generate (e.g., `languages.py` → `languages.tex`).
- Prefer f-strings for string interpolation and keep locale-aware formatting inside helper functions to avoid duplication.
- Keep JSON keys lowerCamelCase to match the current schema consumed in the templates.
- Document non-obvious LaTeX macros with brief comments so downstream editors understand formatting constraints.

## Testing Guidelines
- There are no automated tests; validate changes by running `python main.py` and ensuring both PDFs compile without LaTeX warnings.
- Spot-check the generated `resume/*.tex` files for UTF-8 issues, date formatting, and section ordering whenever you modify templates or input JSON.
- When adjusting locale behaviour, run with both English and Italian datasets to confirm `locale.setlocale` produces the expected month names.

## Commit & Pull Request Guidelines
- Use concise, imperative commit messages (e.g., `Add awards template formatter`) and group related template/data changes together.
- For pull requests, include a summary of affected sections, link any tracking issue, and attach rendered PDFs or key LaTeX diffs so reviewers can compare visual output.
- Call out any required updates to `.env` or data directory layout in the PR description to keep other agents in sync.
