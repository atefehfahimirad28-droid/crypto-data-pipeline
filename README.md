# Crypto Data Pipeline

This project builds a simple ETL pipeline that extracts cryptocurrency prices from the CoinGecko API, transforms the data using Pandas, and loads it into a PostgreSQL database.

## Architecture

API → Extract → Raw JSON → Transform → CSV → PostgreSQL

## Technologies

- Python
- Pandas
- PostgreSQL
- REST API

## How to run

1. Extract data

python scripts/extract_crypto.py

2. Transform data

python scripts/transform_crypto.py

3. Load data into PostgreSQL

python scripts/load_crypto.py