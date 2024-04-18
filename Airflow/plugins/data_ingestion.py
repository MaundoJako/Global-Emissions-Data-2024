import os
import subprocess
from google.cloud import storage  # Change this line

# Rest of your script remains the same

def download_from_kaggle(dataset_name, kaggle_username, kaggle_key, destination_path):
    """
    Download dataset from Kaggle using Kaggle API
    
    Args:
    - dataset_name (str): Kaggle dataset name (e.g., 'kanchana1990/world-air-quality-data-2024-updated')
    - kaggle_username (str): Your Kaggle username
    - kaggle_key (str): Your Kaggle API key
    - destination_path (str): Destination path to save the downloaded dataset
    
    Returns:
    - str: Path to the downloaded dataset
    """
    # Set Kaggle API credentials
    os.environ['KAGGLE_USERNAME'] = kaggle_username
    os.environ['KAGGLE_KEY'] = kaggle_key
    
    # Download dataset from Kagglep
    subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_name, '-p', destination_path])
    
    # Get downloaded file name
    downloaded_file = os.path.join(destination_path, f'{dataset_name.split("/")[-1]}.zip')
   
    return downloaded_file

def upload_to_gcs(bucket_name, source_file, destination_blob_name):
    """
    Upload file to Google Cloud Storage
    
    Args:
    - bucket_name (str): GCS bucket name
    - source_file (str): Path to the source file to upload
    - destination_blob_name (str): Destination blob name in GCS
    
    Returns:
    - None
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    blob.upload_from_filename(source_file)

# Example usage: These are not necessary but I just put these in here for practice. We will be inputting data from the dags file.
if __name__ == "__main__":
    # Set Kaggle credentials
    kaggle_username = 'jakemaund'
    kaggle_key = '84d5599dd3b8c8f375adf7345b1947e2'
    
    # Download dataset from Kaggle
    dataset_name = 'kanchana1990/world-air-quality-data-2024-updated'
    downloaded_file = download_from_kaggle(dataset_name, kaggle_username, kaggle_key, './')
    
    # Upload downloaded file to Cloud Storage
    bucket_name = 'jm-data-lake'
    destination_blob_name = 'data/world_air_quality.csv'
    upload_to_gcs(bucket_name, downloaded_file, destination_blob_name)

