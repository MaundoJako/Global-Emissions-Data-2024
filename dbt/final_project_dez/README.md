    final_project_DEz/
    ├── models/
    │   └── my_model.sql
    └── macros/
        └── ELT_Python_Script.py
        
## Overview

This dbt project (final_project_DEz) is designed to facilitate the Extract, Load, Transform (ELT) process for your data pipeline. It consists of two main components:

  **Models:** dbt models define the SQL transformations to be applied to your data.
  **Macros:** Python scripts used within dbt models to perform custom data processing tasks.


## Description
**1. Models**

  - my_model.sql: This dbt model defines a transformation pipeline. It configures the materialization as a table and invokes a Python script using the run-operation macro. This model orchestrates the ELT process by defining the transformation logic and integrating external Python scripts.

**2. Macros**

  - ELT_Python_Script.py: This Python script contains functions for extracting data from a Google Cloud Storage (GCS) bucket, performing data transformations, and loading the transformed data into Google BigQuery. It is invoked by the my_model.sql model to perform ELT operations.


## Running the Project

  ### Setup dbt Project:
        Clone this repository to your local machine.
        Install dbt following the instructions in the official documentation.
        Navigate to the final_project_DEz directory in your terminal.

  ### Set GCP Credentials:
        Ensure your GCP credentials are correctly set up to allow access to GCS and BigQuery services.

  ### Configure dbt Profiles:
        Update the profiles.yml file in your dbt project directory with credentials for your GCP project.

  ### Run dbt Project (in terminal):
        dbt run

## Verify Results:

   - Check the logs and outputs to ensure the dbt models have been executed successfully and data has been loaded into BigQuery.



# Setting up DBT

### Mac:

Install dbt:

    brew tap dbt-labs/dbt
    brew install dbt


### Windows:

Install dbt:

    Run the following command in PowerShell to install dbt using Chocolatey:

    choco install dbt


### Linux:

sudo apt-get update
sudo apt-get install dbt



## Verify Installation:


    dbt --version


## Creating a Virtual Environment:

### Mac/Linux:

    python3 -m venv dbt-env
    source dbt-env/bin/activate

### Windows:

    python -m venv dbt-env
    .\dbt-env\Scripts\activate
## Installing dbt-bigquery

    python -m pip install dbt-bigquery

## Initializing a dbt Project:

Navigate to the directory where you want to create your dbt project.
Run the following command to initialize a new dbt project:

    dbt init
    
## Verifying

    dbt debug
