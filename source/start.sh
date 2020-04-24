#!/bin/bash
while true; do
    python3 main.py
    echo "[FATAL] crashed with exit code $?.  Respawning... " >&2
    sleep 5
done
