#!/usr/bin/env zsh

uv run ruff format
uv run ruff check
uv run ty check --fix
uv run ty check
uv run pytest
