Install prequisites
  pip install os subprocess google datetime



README.md
Airflow Data Ingestion Plugin

This repository contains the code for an Airflow DAG designed to automate the process of ingesting data from Kaggle into Google Cloud Storage (GCS). The DAG consists of two tasks: downloading data from Kaggle and uploading it to GCS.

Install prequisites
  pip install os subprocess google datetime


Usage
Plugin Files

    data_ingestion.py: This file contains the functions download_from_kaggle() and upload_to_gcs() which are used in the Airflow DAG to download data from Kaggle and upload it to GCS, respectively.

    data_ingestion_dag.py: This file defines the Airflow DAG data_ingestion_dag and specifies the tasks involved in the data ingestion process.

DAG Configuration

    Default Arguments: The default arguments for the DAG are specified in the default_args dictionary. These include the owner, start date, and retry settings.

    Tasks: Two tasks are defined in the DAG:
        download_from_kaggle: Downloads data from Kaggle using the download_from_kaggle() function.
        upload_to_gcs: Uploads the downloaded data to Google Cloud Storage using the upload_to_gcs() function.

    Task Dependencies: The download_task is set to run before the upload_task using the task dependency >>.

Running the DAG

    Ensure that Apache Airflow is installed and running.
    Copy the plugin files (data_ingestion.py and data_ingestion_dag.py) to the Airflow plugins directory.
    Trigger the DAG manually or set up a schedule for it to run automatically.

Plugin Folder
__init__.py

The __init__.py file in the plugin folder serves as an initializer for the Python package. It allows the folder to be treated as a package, making it possible to import modules from within the folder.
setup.py

The setup.py file is used for packaging and distribution. It specifies metadata about the package such as its name, version, and dependencies. In this case, it defines the jm_final_project package with version 0.1 and specifies the required dependencies for the plugin.
Note

To use the Kaggle API for downloading data, you need to obtain a Kaggle API key and replace the placeholder kaggle_key in the data_ingestion_dag.py file with your actual key. Additionally, ensure that your Google Cloud Storage bucket name and file paths are correctly specified in the DAG.

  Kaggle Authentication
      - Create kaggle login
      - My Account
      - Create new token
      - A 'kaggle.json' file will be downloaded.
      - Move kaggle file from your downloads to ~/.kaggle
         - (MacOS) Enter in your terminal: mv /path_to_downloads/kaggle.json /path_to_kaggle/.kaggle/
