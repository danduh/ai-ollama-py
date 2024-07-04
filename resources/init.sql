CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'postgres';
CREATE ROLE root WITH LOGIN SUPERUSER PASSWORD 'password';

CREATE DATABASE vector_db;

\connect vector_db;

CREATE EXTENSION IF NOT EXISTS vector;
-- CREATE TABLE IF NOT EXISTS embeddings (
--   id SERIAL PRIMARY KEY,
--   embedding vector,
--   text text,
--   created_at timestamptz DEFAULT now()
-- );
