# Global-Emissions-Data-2024

Data Engineering Zoomcamp: final project

    Global-Emissions_data-2024/
    ├── Airflow/
    │   ├── dags/
    │   │   └── data_ingestion_dag.py
    │   └── plugins/
    │       ├── __init__.py
    │       ├── data_ingestion.py
    │       └── setup.py
    ├── Data/
    │   ├── cleaned_data.parquet
    │   └── world_air_quality.csv
    ├── Terraform/
    │   ├── main.tf
    │   └── bigquery.tf
    └── dbt/
        └── final_project_DEz/
            ├── models/
            │   └── my_model.sql
            └── macros/
                └── ELT_Python_Script.py



## Introduction

The purpose of this project is for learning purposes, as part of the Data Engineering Zoomcamp 2024 final project. 

The problem which this project solves is that working with the kaggle data requires transformations and storage for future data batches. Therefore, this project provides automated ELT which can be repeated in the future

To achieve this, data is extracted using Airflow; loaded into  GCP bucket; transformed and loaded into BigQuery via dbt; then visualised using Looker.

The data is global emissions data (2024), imported from Kaggle.

## Dataset
- https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated/data
  
I have provided the raw csv file within this repository, can be found via: Data / world_air_quality. Additionally, I have provided a cleaned partition file


## Tools
- GCP
- Terraform
- Python
- Airflow
- dbt
- Looker Studio


## Solution

![image](https://github.com/MaundoJako/Global-Emissions-Data-2024/assets/91381193/b29edb4b-8d8d-42be-9d16-c5d06db89869)


## Dashboard:

![image](https://github.com/MaundoJako/Global-Emissions-Data-2024/assets/91381193/57803d5f-5265-4822-9858-40f7986e1ed6)


## Prequisites
**GCP (Google Cloud Platform)**

 No specific installation required. 
 
 Access GCP services via web console or Google Cloud SDK. 
 
 - Configuration: Install Google Cloud SDK: Follow instructions here for your operating system. 
  
 - Authenticate Google Cloud SDK: Run gcloud auth login and follow the prompts to authenticate. 
  
 - Set default project: Run gcloud config set project <project_id> to set the default project.

**Terraform** 
  
    pip install terraform

**Python**

    pip install python
    
    pip install pandas google-cloud-storage google-cloud-bigquery

**Airflow**

    pip install apache-airflow

**dbt (data build tool)** 

    pip install dbt

**Looker Studio**

- Sign up for a Looker Studio account and log in.
- Configure connections to your data sources within Looker.




# Instructions
Further instructions can be found within each module's ReadMe, these instructions are at a higher level.

**1. Set up infrastructure --- Terraform**
   - Open Terraform/
   - Deploy main.tf and bigquery.tf files
       - Make changes to names, where applicable. Feel free to add further resources or to use variables for best practice, however, the current terraform code works just fine for what this project needs.
   - Add your GCP credentials to your machine.
   - Terraform Init
   - Terraform Apply

**2. Review infrastructure --- GCP**
   - Login to GCP
   - Check that your vm instance, bucket, and bigquery file is setup.

**3. Extract Data --- Airflow**
   - Open Airflow/plugins
   - Run data_ingestion.py
   - Open Airflow/dags
   - Run data_ingestion_dag.py
     - The dag file will call the plugin, you will need both for the Airflow to work
   - Set up cron job to ensure code runs on a schedule, current code is assigned to run monthly.

**4. Transform and Load --- dbt**
   - Open dbt/final_project_dez/
   - Open models/
   - Save my_model.sql
   - Open macros/
   - Save ELT_Python_Scripy.py
   - Run in Terminal : dbt run  
     - A BigQuery folder and file will be created, however you specified in your creation.
     

**5. Data Visualisation --- Looker**
   - Navigate to Looker Studio via your search engine
   - Create (top left)
   - Data Source
   - BigQuery
   - Create any visualisation you wish
  

  
