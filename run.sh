#!/usr/bin/env bash
set -e

# Prefer the modern `docker compose` command if available
COMPOSE="docker compose"
if ! docker compose version >/dev/null 2>&1; then
    COMPOSE="docker-compose"
fi

if [ "$1" = "down" ]; then
    $COMPOSE down
else
    $COMPOSE up --build
fi
