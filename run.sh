#!/usr/bin/env bash
set -e
if [ "$1" = "down" ]; then
    docker-compose down
else
    docker-compose up --build
fi
