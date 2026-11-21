#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
command -v gradle >/dev/null || { echo "Gradle CLI 8.13 required to generate a standard wrapper; no wrapper JAR bundled." >&2; exit 2; }
gradle wrapper --gradle-version 8.13 --distribution-type bin
printf '%s\n' 'Wrapper generated. Review generated files before commit.'
