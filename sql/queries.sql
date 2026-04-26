-- show all data
SELECT * FROM crypto_prices;

-- average price per coin
SELECT coin, AVG(price_usd)
FROM crypto_prices
GROUP BY coin;

-- max price per coin
SELECT coin, MAX(price_usd)
FROM crypto_prices
GROUP BY coin;

-- latest price per coin
SELECT DISTINCT ON (coin)
coin, price_usd, extracted_at
FROM crypto_prices
ORDER BY coin, extracted_at DESC;