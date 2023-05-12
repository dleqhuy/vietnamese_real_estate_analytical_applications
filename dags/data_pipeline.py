from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

import scripts.extract_estate_data
import scripts.sql_statements
import pandas as pd

default_args = {
    'owner': 'huyduong',
    'start_date': days_ago(0),
    'email': ['huyduonglequang@gmail.com'],
    'email_on_failure': False,
    'email_on-retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}



with DAG(
    dag_id='automate_data_pipeline',
    default_args=default_args,
    description='Data pipeline to process nhatot.com',
    start_date=datetime(2023, 5, 7),

    schedule_interval='@daily',
    tags=['data-pipeline', 'etl', 'information']
) as dag:
    
    # start_operator = DummyOperator(task_id='start_pipeline')
    
    # end_operator = DummyOperator(task_id='stop_pipeline')
    
    create_estate_data_table = PostgresOperator(
            task_id='create_estate_data_table',
            postgres_conn_id='postgres_default',
            sql=scripts.sql_statements.create_estate_data_table,
                            )

    extract_estate_data = PythonOperator(
            task_id='extract_estate_data_raw',
            python_callable=scripts.extract_estate_data.main,
            op_kwargs={'path_csv': 'dags/crawler/area.csv'}

        )
    
    create_estate_data_table >> extract_estate_data
    