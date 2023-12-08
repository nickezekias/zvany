#!/bin/bash

#export env variables from .env file
export $(grep -v '^#' .env | xargs -d '\n')

#init database with data
#mariadb -u zvany -p < src/app/db/init_db.min.sql

cd src
alembic upgrade head

cd ../

# exec python -m uvicorn --reload --host $APP_HOST --port $APP_PORT src.main:app
python -m uvicorn --reload --host $APP_HOST --port $APP_PORT src.main:app