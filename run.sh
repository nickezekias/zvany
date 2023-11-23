#!/bin/bash
export $(grep -v '^#' .env | xargs -d '\n')

./prestart.sh

exec python -m uvicorn --reload --host $APP_HOST --port $APP_PORT src.main:app