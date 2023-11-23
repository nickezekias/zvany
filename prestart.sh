#start db
export $(grep -v '^#' .env | xargs -d '\n')

#mariadb -u zvany -p < src/app/db/init_db.min.sql

# Run migrations
cd src
alembic upgrade head

#cd back to project root
# cd ../../