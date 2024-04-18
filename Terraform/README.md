# Terraform Configuration
    
    ├── Terraform/
    │   ├── main.tf
    │   └── bigquery.tf

## Overview

Terraform is an open-source infrastructure as code software tool created by HashiCorp. It allows users to define and provision data center infrastructure using a high-level configuration language known as HashiCorp Configuration Language (HCL), or optionally JSON.

This Terraform configuration provides infrastructure resources for your project, including a Google Compute Engine instance and a Google Cloud Storage bucket.

## Terraform Files

    main.tf: Defines the Google Compute Engine instance and network resources.
    bigquery.tf: Defines the Google BigQuery dataset resource.

## How to Use

### Prerequisites

Before using this Terraform configuration, ensure that you have:

  - A Google Cloud Platform (GCP) account with appropriate permissions.
    
  - Terraform installed on your local machine.

  - Clone Repository: Clone this repository to your local machine.

  - Navigate to Terraform Directory: Navigate to the Terraform directory within the cloned repository.

  - Terminal:

        cd Terraform

### Initialize Terraform: Run the terraform init command to initialize Terraform and download the required providers.

    terraform init

Review Configuration: Review the main.tf and bigquery.tf files to ensure that the configuration matches your requirements.

### Apply Configuration: Run the terraform apply command to create the infrastructure resources on GCP.

    Terraform apply

Confirm Changes: Review the proposed changes and enter yes when prompted to confirm.

Access Resources: Once the Terraform script has completed execution, you can access the provisioned resources on Google Cloud Platform.

### Cleanup (Optional): To delete the provisioned resources and avoid incurring charges, run the terraform destroy command.

    terraform destroy

Confirm Destruction: Review the proposed changes and enter yes when prompted to confirm resource deletion.

