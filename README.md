Crypto Data Pipeline (ETL with Docker & PostgreSQL)
📌 Overview
This project implements a modular ETL (Extract, Transform, Load) pipeline for collecting real-time cryptocurrency market data from the CoinGecko API and storing it in a PostgreSQL database.

The pipeline is designed with a data engineering mindset, focusing on clean architecture, reproducibility, and containerized execution using Docker.

🧠 Key Features
Modular ETL Pipeline: Clear separation between Extraction, Transformation, and Loading logic.

API Ingestion: Real-time data fetching using Python Requests.

Data Processing: Cleaning and normalization using Pandas.

Relational Storage: Structured data storage in PostgreSQL.

Containerization: Fully orchestrated environment using Docker Compose.

Security: Configurable environment variables via .env files.

🏗️ System Architecture
The pipeline follows a structured batch-processing workflow:

Extract: Fetch cryptocurrency data from CoinGecko API (JSON format).

Transform: Normalize data, handle missing values, and structure it into tabular format using Pandas.

Load: Upsert/Insert data into the PostgreSQL crypto_prices table.

🐳 Docker Architecture
The application runs in isolated containers within a shared bridge network:

crypto_app: The Python environment that executes the ETL scripts.

crypto_postgres: The database engine for persistent storage.

Volumes: Dedicated Docker volumes to ensure data persists even after container restarts.

📂 Project Structure
Plaintext
crypto-data-pipeline/
├── scripts/
│   ├── extract.py      # API fetching logic
│   ├── transform.py    # Data cleaning & Pandas logic
│   ├── load.py         # Database insertion logic
│   └── main.py         # Pipeline orchestrator
├── config/
│   └── db_config.py    # Database connection settings
├── .env.example        # Template for environment variables
├── docker-compose.yml  # Docker services configuration
├── Dockerfile          # Python environment definition
└── requirements.txt    # Python dependencies
⚙️ Setup & Execution
1. Clone the Repository
Bash
git clone https://github.com/YOUR_USERNAME/crypto-data-pipeline.git
cd crypto-data-pipeline
2. Configure Environment
Bash
cp .env.example .env
Note: Open .env and update your database credentials if necessary.

3. Start Docker Services
Bash
docker compose up -d --build
4. Run the ETL Pipeline
Bash
docker exec -it crypto_app python scripts/main.py
🗄️ Database Schema
Table: crypto_prices
Column	Type	Description
coin	TEXT	Cryptocurrency name (e.g., Bitcoin)
price_usd	FLOAT	Current price in USD
extracted_at	TIMESTAMP	Execution timestamp
🔍 Data Verification
To verify the data directly inside the container:

Access PostgreSQL:

Bash
docker exec -it crypto_postgres psql -U postgres -d crypto_db
Run Query:

SQL
SELECT * FROM crypto_prices LIMIT 10;
🚀 Future Improvements
[ ] Orchestration: Integrate Apache Airflow for automated scheduling.

[ ] Cloud Storage: Add a stage to store raw JSON data in AWS S3 (Data Lake).

[ ] Monitoring: Build a dashboard using Streamlit or Grafana.

[ ] Resilience: Implement advanced error handling and Slack/Email alerts.

💡 Key Learnings
Designing modular, maintainable ETL architectures.

Managing relational schemas for time-series market data.

Containerizing multi-service applications for DevOps-ready deployments.

👤 Author
Atefeh Fahimirad
Junior Data Engineer

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: [Your LinkedIn Profile Li
