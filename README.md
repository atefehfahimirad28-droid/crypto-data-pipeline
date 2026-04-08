🚀 Crypto Data Pipeline (ETL with Docker & PostgreSQL)

"Python" (https://img.shields.io/badge/python-3.9+-blue.svg)

"Docker" (https://img.shields.io/badge/docker-%230db7ed.svg)

"PostgreSQL" (https://img.shields.io/badge/PostgreSQL-316192.svg)

"Pandas" (https://img.shields.io/badge/pandas-%23150458.svg)

---

📌 Overview

This project implements a modular ETL (Extract, Transform, Load) pipeline for collecting cryptocurrency market data from the CoinGecko API and storing it in a PostgreSQL database.

The pipeline is designed with a data engineering mindset, focusing on clean architecture, reproducibility, and containerized execution using Docker.

---

🧠 Key Features

- Modular ETL pipeline (Extract / Transform / Load separation)
- API data ingestion using Python (Requests)
- Data cleaning and transformation with Pandas
- Relational storage in PostgreSQL
- Fully containerized environment using Docker Compose
- Configurable environment using ".env"

---

🏗️ System Architecture

The pipeline follows a structured batch-processing workflow:

CoinGecko API
      ↓
Extract (Python + Requests)
      ↓
Transform (Pandas)
      ↓
Load (PostgreSQL)

---

🐳 Docker Architecture

The application runs in isolated containers:

Services:

- "crypto_app" → Executes ETL pipeline
- "crypto_postgres" → PostgreSQL database

Network:

- Bridge network for inter-container communication

Volumes:

- Persistent storage for database data

---

🔄 Data Pipeline Flow

1. Extract
   
   - Fetch cryptocurrency data from CoinGecko API
   - Handle API responses (JSON format)

2. Transform
   
   - Normalize and clean data
   - Convert into structured tabular format

3. Load
   
   - Insert data into PostgreSQL table
   - Ensure consistent schema

---

## 📂 Project Structure

```bash
crypto-data-pipeline/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── config/
│   └── db_config.py
│
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── requirements.txt

---

⚙️ Setup & Execution

1. Clone Repository

git clone https://github.com/YOUR_USERNAME/crypto-data-pipeline.git
cd crypto-data-pipeline

---

2. Configure Environment

cp .env.example .env

Update database credentials if needed.

---

3. Start Docker Services

docker compose up -d --build

---

4. Run ETL Pipeline

docker exec -it crypto_app python scripts/main.py

---

🗄️ Database Schema

Table: crypto_prices

Column| Type| Description
coin| TEXT| Cryptocurrency name
price_usd| FLOAT| Price in USD
extracted_at| TIMESTAMP| Extraction timestamp

---

🔍 Data Verification

Access PostgreSQL:

docker exec -it crypto_postgres psql -U postgres -d crypto_db

Run query:

SELECT * FROM crypto_prices LIMIT 10;

---

📜 Logging & Debugging

The pipeline provides basic logging for each stage:

[INFO] Extracted data from API
[INFO] Transformed data successfully
[INFO] Loaded data into PostgreSQL

Check container logs:

docker compose logs -f

---

🧰 Common Operations

Stop containers:

docker compose down

Remove volumes:

docker compose down -v

Rebuild containers:

docker compose up -d --build

---

🚀 Future Improvements

- Add orchestration with Apache Airflow
- Implement retry and error handling mechanisms
- Store raw data in AWS S3
- Add scheduling (daily batch pipeline)
- Build monitoring dashboards (Streamlit / BI tools)

---

💡 Key Learnings

- Designing modular ETL pipelines
- Working with REST APIs and JSON data
- Data transformation using Pandas
- PostgreSQL database integration
- Docker-based development environments

---

👤 Author

Atefeh Fahimirad
Junior Data Engineer
