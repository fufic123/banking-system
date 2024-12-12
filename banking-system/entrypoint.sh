#!/usr/bin/env bash
set -e

echo "Waiting for Postgres..."
until pg_isready -h db -p 5432 -U user; do
  sleep 2
done

echo "Postgres is ready, running migrations..."
psql postgresql://user:password@db:5432/banking_db -f sql/01_extensions.sql
psql postgresql://user:password@db:5432/banking_db -f sql/02_create_tables.sql
psql postgresql://user:password@db:5432/banking_db -f sql/03_create_indexes.sql
psql postgresql://user:password@db:5432/banking_db -f sql/04_insert_data.sql
psql postgresql://user:password@db:5432/banking_db -f sql/05_views.sql
psql postgresql://user:password@db:5432/banking_db -f sql/06_triggers.sql

echo "Migrations done, starting the server..."
exec "$@"
