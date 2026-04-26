import json
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting transform step")

try:
    # read raw JSON file
    with open("data/raw/crypto_prices.json", "r") as f:
        data = json.load(f)

    logging.info("Raw JSON file loaded")

    rows = []

    # validate and transform data
    for coin, values in data.items():
        if "usd" not in values:
            logging.warning(f"Missing USD price for {coin}")
            continue

        rows.append({
            "coin": coin,
            "price_usd": values["usd"],
            "extracted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # convert to dataframe
    df = pd.DataFrame(rows)

    print(df)

    logging.info("Data transformed into DataFrame")

    # save processed data
    df.to_csv("data/processed/crypto_prices_processed.csv", index=False)

    logging.info("CSV file saved to data/processed/crypto_prices_processed.csv")

except FileNotFoundError:
    logging.error("Raw JSON file not found")
    print("Error: raw data file not found")

except json.JSONDecodeError:
    logging.error("Invalid JSON format")
    print("Error: JSON file is corrupted")

except Exception as e:
    logging.error(f"Unexpected error: {e}")
    print(f"Unexpected error: {e}")