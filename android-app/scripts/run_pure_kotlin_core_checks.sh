#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
command -v kotlinc >/dev/null || { echo "Missing kotlinc" >&2; exit 2; }
command -v java >/dev/null || { echo "Missing java" >&2; exit 2; }
OUT="$(mktemp -d)"
trap 'rm -rf "$OUT"' EXIT
kotlinc \
  app/src/main/java/vn/toeiclearning/alpha/domain/AlphaModels.kt \
  app/src/main/java/vn/toeiclearning/alpha/domain/SyntheticCatalogue.kt \
  tests/pure-kotlin/AlphaCoreSmokeTest.kt \
  -include-runtime -d "$OUT/alpha-pure-core.jar"
java -jar "$OUT/alpha-pure-core.jar"
