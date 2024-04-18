import pandas as pd
from google.cloud import storage
from google.cloud import bigquery

def extract_data_from_gcp_bucket(bucket_name, source_blob_name):
    """
    Extracts data from a file in a GCP bucket and returns it as a DataFrame.
    
    Args:
        bucket_name (str): Name of the GCP bucket.
        source_blob_name (str): Name of the file in the bucket to extract.
        
    Returns:
        pd.DataFrame: Extracted data as a DataFrame.
    """
    # Initialize a client
    storage_client = storage.Client()
    
    # Get the bucket
    bucket = storage_client.bucket(bucket_name)
    
    # Get the blob (file) from the bucket
    blob = bucket.blob(source_blob_name)
    
    # Download the blob's content and read it into a DataFrame
    df = pd.read_csv(blob.download_as_string().decode('utf-8'), sep=';')
    
    return df

def load_data_to_bigquery(df, project_id, dataset_id, table_id, partition_column=None):
    """
    Loads data from a DataFrame into BigQuery.
    
    Args:
        df (pd.DataFrame): DataFrame containing the data to load.
        project_id (str): ID of the GCP project containing the BigQuery dataset.
        dataset_id (str): ID of the BigQuery dataset.
        table_id (str): ID of the BigQuery table to load the data into.
        partition_column (str, optional): Name of the column to partition on. Defaults to None.
    """
    # Initialize a client
    bigquery_client = bigquery.Client(project=project_id)
    
    # Define the dataset and table references
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    
    # Convert DataFrame to JSON records and load into BigQuery
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE  # Overwrite the existing table
    
    if partition_column:
        job_config.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field=partition_column
        )
    
    job = bigquery_client.load_table_from_dataframe(
        df, table_ref, job_config=job_config
    )
    
    job.result()  # Wait for the job to complete

# Set GCP project and BigQuery dataset info
project_id = 'praxis-wall-411617'
dataset_id = 'final_project_DEz_BQ'
table_id = 'final_project_JM'  

# Extract data from GCP bucket
bucket_name = 'jm-data-lake'
source_blob_name = 'world_air_quality.csv'  
df = extract_data_from_gcp_bucket(bucket_name, source_blob_name)

# Perform data transformations
# Filter data for United Kingdom
gb_data = df[df['Country Label'] == 'United Kingdom']

# Data Cleaning
country_mapping = {
    'XK': 'Kosovo',
    'KV': 'Kosovo',
    'UC': 'Curacao',
    'CW': 'Curacao',
    'AQ': 'American Samoa',
    'AJ': 'Azerbaijan',
    'BK': 'Bosnia and Herzegovina',
    'CE': 'Sri Lanka',
    'IZ': 'Iraq',
    'KU': 'Kuwait',
    'MK': 'North Macedonia',
    'TI': 'Tajikistan',
    'TX': 'Turkmenistan',
    'VM': 'Vietnam'
}
df['Country Label'] = df['Country Code'].replace(country_mapping)

columns_to_fill = ['City', 'Location', 'Coordinates']
for column in columns_to_fill:
    df[column] = df[column].fillna('Missing data')

# Drop duplicates
df.drop_duplicates(inplace=True)

# Drop rows with negative values in 'Value' column
df = df[df['Value'] >= 0]

# Drop rows with units to be excluded
units_to_drop = ['c', 'particles/cm³', '%']
df = df[~df['Unit'].isin(units_to_drop)]

# Loading data to GCP BigQuery with partitioning on 'Date' column
load_data_to_bigquery(df, project_id, dataset_id, table_id, partition_column='Date')
