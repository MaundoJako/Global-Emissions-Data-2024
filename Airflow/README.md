Install prequisites
  pip install os subprocess google datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from plugins.data_ingestion.data_ingestion import download_from_kaggle, upload_to_gcs #direction will be different in Git for reading simplicity. If trying to replicate, change the from command to the path to your plugin with same format as here.

    
  Kaggle Authentication
      - Create kaggle login
      - My Account
      - Create new token
      - A 'kaggle.json' file will be downloaded.
      - Move kaggle file from your downloads to ~/.kaggle
         - (MacOS) Enter in your terminal: mv /path_to_downloads/kaggle.json /path_to_kaggle/.kaggle/
