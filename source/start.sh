#!/bin/bash
while :
do
    python3 main.py
    echo "[FATAL] 'olx-destroy' crashed with exit code $?. Restarting...">> log
end
