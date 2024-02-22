#!/bin/bash
#export env variables from .env file
# export $(grep -v '^#' .env | xargs -d '\n')

exec python -m uvicorn --reload --host $APP_HOST --port $APP_PORT src.main:app