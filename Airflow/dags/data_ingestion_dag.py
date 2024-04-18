from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from plugins.data_ingestion.data_ingestion import download_from_kaggle, upload_to_gcs #direction will be different in Git for reading simplicity. If trying to replicate, change the from command to the path to your plugin with same format as here.

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 18), # This is when it will run, adjust accordingly.
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
with DAG('data_ingestion_dag', default_args=default_args, schedule_interval='@monthly') as dag:    # Scheduled to run Monthly
    # Define tasks
    download_task = PythonOperator(
        task_id='download_from_kaggle',
        python_callable=download_from_kaggle,
        op_kwargs={
            'dataset_name': 'kanchana1990/world-air-quality-data-2024-updated',
            'kaggle_username': 'jakemaund', # Adjust accordingly
            'kaggle_key': '$$$$$$$$$$$$$$$$$', # I have removed my key here for security, please follow instructions in ReadME file to get your kaggle key.
            'destination_path': '/tmp/' # Adjust accordingly
        }
    )
    
    upload_task = PythonOperator(
        task_id='upload_to_gcs',
        python_callable=upload_to_gcs,
        op_args=['jm-data-lake', '/tmp/world-air-quality-data-2024-updated.zip', 'data/world_air_quality.csv'] # Adjust Accordingly --- bucket name, your saved file, where you will be saving your file in bucket/name of file
    )

    # Define task dependencies
    download_task >> upload_task
