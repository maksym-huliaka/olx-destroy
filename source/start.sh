#!/bin/bash
while true; do
    python3 main.py >> logfile.log 2&>1
    echo "[FATAL] crashed with exit code $?.  Respawning... " >&2
    sleep 5
done
