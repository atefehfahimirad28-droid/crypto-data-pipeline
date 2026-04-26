import requests
import json
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting extract step")

# API endpoint for CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price"

# parameters for the API request
params = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd"
}

try:
    # send request
    response = requests.get(url, params=params ,timeout=15 )

    # raise error if request failed
    response.raise_for_status()

    # convert response to JSON
    data = response.json()

    # print data
    print(data)

    logging.info("Data extracted from API successfully")

    # save raw data to file
    with open("data/raw/crypto_prices.json", "w") as f:
        json.dump(data, f, indent=4)

    logging.info("Raw data saved to data/raw/crypto_prices.json")

except requests.exceptions.RequestException as e:
    logging.error(f"Error during API request: {e}")
    print(f"Error during API request: {e}")