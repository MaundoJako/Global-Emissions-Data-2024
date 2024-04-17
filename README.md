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

  
