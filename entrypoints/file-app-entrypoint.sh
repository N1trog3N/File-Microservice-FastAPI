#!/bin/bash
set -e

echo "Uvicorn is starting..."
exec uvicorn src.presentation.main:app --host 0.0.0.0 --port 8090 --reload
