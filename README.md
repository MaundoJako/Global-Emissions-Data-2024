# Global-Emissions-Data-2024

Data Engineering Zoomcamp: final project

# Introduction

The purpose of this project is for learning purposes, as part of the Data Engineering Zoomcamp 2024 final project. 

The problem which this project solves is that working with the kaggle data requires transformations and storage for future data batches. Therefore, this project provides automated ELT which can be repeated in the future

To achieve this, data is extracted using Airflow; loaded into  GCP bucket; transformed and loaded into BigQuery via dbt; then visualised using Looker.

The data is global emissions data (2024), imported from Kaggle.

# Dataset
- https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated/data
  
I have provided the raw csv file within this repository, can be found via: Data / world_air_quality. Additionally, I have provided a cleaned partition file


# Tools
- GCP
- Terraform
- Python
- Airflow
- dbt
- Looker Studio


# Solution

![image](https://github.com/MaundoJako/Global-Emissions-Data-2024/assets/91381193/b29edb4b-8d8d-42be-9d16-c5d06db89869)


# Dashboard:

![image](https://github.com/MaundoJako/Global-Emissions-Data-2024/assets/91381193/57803d5f-5265-4822-9858-40f7986e1ed6)


# Prequisites
GCP (Google Cloud Platform)

    Installation: No specific installation required. Access GCP services via web console or Google Cloud SDK.
    Configuration:
        Install Google Cloud SDK: Follow instructions here for your operating system.
        Authenticate Google Cloud SDK: Run gcloud auth login and follow the prompts to authenticate.
        Set default project: Run gcloud config set project <project_id> to set the default project.

Terraform

    Installation: Install Terraform CLI using the following commands:

    bash

    brew install terraform  # For macOS

    For other platforms, refer to the official installation guide.
    Configuration:
        No additional configuration required for basic usage.
        Create Terraform configuration files (.tf) to define infrastructure resources.

Python

    Installation: Install Python 3.x from the official Python website or via package manager:

    bash

brew install python  # For macOS

Configuration:

    Install necessary Python packages using pip:

        pip install pandas google-cloud-storage google-cloud-bigquery

Airflow

    Installation: Install Apache Airflow using pip:

pip install apache-airflow

Configuration:

    Initialize Airflow database:

    csharp

airflow db init

Start Airflow web server and scheduler:

css

        airflow webserver --port 8080
        airflow scheduler

dbt (data build tool)

    Installation: Install dbt CLI using pip:

    pip install dbt

    Configuration:
        Create a dbt project: Run dbt init <project_name> to initialize a new dbt project.
        Configure dbt profiles: Edit ~/.dbt/profiles.yml to define database connections.

Looker Studio

    Installation: Access Looker Studio via web browser. No local installation required.
    Configuration:
        Sign up for a Looker Studio account and log in.
        Configure connections to your data sources within Looker.

# Instructions
1. Set up infrastructure
   - Deploy the main.tf, then the bigquery.tf files.
   - Make changes to names, where applicable. Feel free to add further resources or to use variables for best practice, however, the current terraform code works just fine.
   - You will need to add your GCP credentials to your machine.
   - Use Terraform Init, and Terraform Apply.

2. Review infrastructure
   - Infrastructure should be all set up, review to make sure you have your vm instance, bucket, and bigquery set up.

3. Run Workflow
   - Time to get the data, follow the jupyter notebook
   - You might need to pip install some prequisites.
   - Kaggle Authentication
      - Create kaggle login
      - My Account
      - Create new token
      - A 'kaggle.json' file will be downloaded.
      - Move kaggle file from your downloads to ~/.kaggle
         - (MacOS) Enter in your terminal: mv /path_to_downloads/kaggle.json /path_to_kaggle/.kaggle/
  - Download into parquet (change path accordingly), upload to GCP storage (change path accordingly)

4. Upload to BigQuery
   - Navigate to your GCP BigQuery folder
   - Create new table
   - Source: Bucket
   - Select your newly created parquet file.
   - External table
   - Auto Schema
   - Save
   - Test it is working by running a simple SQL query in BigQuery.

5. Data Visualisation - Looker Studio
   - Navigate to Looker Studio via your search engine
   - Create (top left)
   - Data Source
   - BigQuery
   - Create any visualisation you wish
  
6. Future work
   - Automate workflow using Docker, creating a package and calling using a workflow tool perhaps Mage.
   - Find a better visualisation tool as Looker studio is limited. 

  
