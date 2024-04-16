from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from plugins.data_ingestion.data_ingestion import download_from_kaggle, upload_to_gcs

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
with DAG('data_ingestion_dag', default_args=default_args, schedule_interval=None) as dag:
    
    # Define tasks
    download_task = PythonOperator(
        task_id='download_from_kaggle',
        python_callable=download_from_kaggle,
        op_kwargs={
            'dataset_name': 'kanchana1990/world-air-quality-data-2024-updated',
            'kaggle_username': 'jakemaund',
            'kaggle_key': '84d5599dd3b8c8f375adf7345b1947e2',
            'destination_path': '/tmp/'
        }
    )
    
    upload_task = PythonOperator(
        task_id='upload_to_gcs',
        python_callable=upload_to_gcs,
        op_args=['your_bucket_name', '/tmp/world-air-quality-data-2024-updated.zip', 'data/world_air_quality.csv']
    )

    # Define task dependencies
    download_task >> upload_task
