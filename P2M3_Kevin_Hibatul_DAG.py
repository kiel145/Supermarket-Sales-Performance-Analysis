import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import psycopg2 as db
import pandas as pd
from elasticsearch import Elasticsearch, helpers


# Fetch from PostgreSQL

def fetch_postgre():
    conn = db.connect(
        database="Milestone3",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432"
    )

    df = pd.read_sql("SELECT * FROM table_m3", con=conn)

    df.to_csv(
        "/opt/airflow/dags/P2M3_kevin_hibatul_data_raw.csv",
        index=False
    )


# Data Cleaning

def clean_data():
    df = pd.read_csv("/opt/airflow/dags/P2M3_kevin_hibatul_data_raw.csv")

    df = df.dropna()
    df = df.drop_duplicates()

    df.columns = (
        df.columns
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("%", "percent", regex=False)
        .str.strip()
        .str.replace("-", " ", regex=False)
        .str.replace(" ", "_", regex=False)
        .str.lower()
    )

    df.to_csv(
        "/opt/airflow/dags/P2M3_kevin_hibatul_data_clean.csv",
        index=False
    )


# Load to Elasticsearch

def load_elastic():
    es = Elasticsearch("http://elasticsearch:9200")

    df = pd.read_csv("/opt/airflow/dags/P2M3_kevin_hibatul_data_clean.csv")
    records = df.to_dict(orient="records")

    actions = [
        {
            "_index": "table_m3",
            "_source": record
        }
        for record in records
    ]

    helpers.bulk(es, actions)

# DAG Definition

default_args = {
    "owner": "kevin_hibatul",
    "start_date": dt.datetime(2024, 11, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="P2M3_kevin_hibatul_DAG",
    default_args=default_args,
    schedule_interval="10 9 * * 6",
    catchup=False
) as dag:

    fetchPostgre = PythonOperator(
        task_id="fetch_postgre_data",
        python_callable=fetch_postgre
    )

    cleanData = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data
    )

    uploadElastic = PythonOperator(
        task_id="upload_to_elastic",
        python_callable=load_elastic
    )

    fetchPostgre >> cleanData >> uploadElastic
