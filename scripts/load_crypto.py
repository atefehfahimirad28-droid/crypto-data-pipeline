import pandas as pd
import psycopg2
import logging
from scripts.config import DB_CONFIG

# =========================
# Logging setup
# =========================
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_crypto_data():
    conn = None
    cursor = None
    try:
        logging.info("Starting load step")

        # =========================
        # Read data
        # =========================
        df = pd.read_csv("data/processed/crypto_prices_processed.csv")

        # =========================
        # Connect to DB
        # =========================
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # =========================
        # Create table
        # =========================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            coin TEXT,
            price_usd FLOAT,
            extracted_at TIMESTAMP
        );
        """)

        # =========================
        # Prepare data for bulk insert
        # =========================
        data = [
            (row["coin"], row["price_usd"], row["extracted_at"])
            for _, row in df.iterrows()
        ]

        # =========================
        # Bulk insert (professional)
        # =========================
        cursor.executemany("""
            INSERT INTO crypto_prices (coin, price_usd, extracted_at)
            VALUES (%s, %s, %s)
        """, data)

        conn.commit()

        logging.info(f"Loaded {len(data)} records into PostgreSQL")

    except Exception as e:
        logging.error(f"Error in load step: {str(e)}")
        raise

    finally:
       if cursor:
         cursor.close()
       if conn:
           conn.close()
       logging.info("Database connection closed")


if __name__ == "__main__":
    load_crypto_data()