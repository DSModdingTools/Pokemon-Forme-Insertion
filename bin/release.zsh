#!/usr/bin/env zsh

set -eux

cd "$(git rev-parse --show-toplevel)"
rm -rf "dist"
uv version --bump=patch
git commit -am "[build] bump minor version"
version="$(uv version --short)"
tagname="release/$version"
uv run pyinstaller -y --onefile main.py
chmod +x dist/your_script
git tag "$tagname"
git push origin tag "$tagname"
gh release create --draft --fail-on-no-commits --generate-notes --verify-tag "$tagname" dist/main
