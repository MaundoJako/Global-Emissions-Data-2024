# Global-Emissions-Data-2024

Data Engineering Zoomcamp: final project

# Introduction

This is a simple but efficient package that extracts data, cleans then uploads to a GCP bucket. It was originally intended to use dbt for trasformations, however, using Jupter Notebooks worked just as well. 

This repository uses 2024 global emissions data, the purpose of this work is extract valuable data, clean and read this data, then visualise it efficiently. This was done for educational purposes, all work is my own.

# Dataset
- https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated/data
  
I have provided the raw csv file within this repository, can be found via: Data / world_air_quality. Additionally, I have provided a cleaned partition file, which is the same one I use to upload to my GCP datalake. 


# Tools
- GCP
- Terraform
- Jupyter Notebook
- Looker Studio


# Solution

![image](https://github.com/MaundoJako/Global-Emissions-Data-2024/assets/91381193/c06a1afa-84bd-49c4-bcd6-d59d80a66a6f)


# Dashboard:

![image](https://github.com/MaundoJako/Global-Emissions-Data-2024/assets/91381193/57803d5f-5265-4822-9858-40f7986e1ed6)

