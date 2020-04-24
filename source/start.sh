#!/bin/bash

(
    until python3 main.py; do
        echo "MyApp crashed with exit code $?.  Respawning... " >&2
        sleep 5
    done
) &
