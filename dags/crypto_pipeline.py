from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import os

OUTPUT_PATH = '/opt/airflow/dags/crypto_prices.csv'

def extract_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,eur,gbp,jpy"
    response = requests.get(url)
    return response.json()

def transform_and_load_data(ti):
    raw_data = ti.xcom_pull(task_ids='extract_data')
    df = pd.DataFrame(raw_data).transpose()
    df['timestamp'] = datetime.now()
    
    file_exists = os.path.isfile(OUTPUT_PATH)
    df.to_csv(OUTPUT_PATH, mode='a', header=not file_exists, index=True)
    print("Updated Data with 4 Currencies (USD, EUR, GBP, JPY):")
    print(df)

with DAG(
    dag_id='crypto_data_pipeline_v1',
    start_date=datetime(2026, 4, 1),
    schedule_interval='@hourly',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_crypto_data
    )

    transform_load_task = PythonOperator(
        task_id='transform_and_load_data',
        python_callable=transform_and_load_data
    )

    extract_task >> transform_load_task