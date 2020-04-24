until main.py; do
    echo "[FATAL] 'olx-destroy' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
