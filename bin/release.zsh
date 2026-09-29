#!/usr/bin/env zsh

set -eux

cd "$(git rev-parse --show-toplevel)"
rm -rf "dist"
uv version --bump=patch
version="$(uv version --short)"
tagname="release/$version"
uv run pyinstaller -y --onefile main.py
git tag "$tagname"
git push --tags
gh release create --draft --fail-on-no-commits --generate-notes --verify-tag "$tagname" dist/main
