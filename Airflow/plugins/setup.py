from setuptools import setup, find_packages

setup(
    name='jm_final_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    'apache-airflow',  # Required for Airflow
    'google-cloud-storage'  # Required for interacting with Google Cloud Storage
    ]

)
