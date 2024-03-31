resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "final_project_dataset"
  friendly_name               = "bq-dataset"
  description                 = "BigQuery dataset for DE Zoomcamp final project."
  location                    = "EU"
  default_table_expiration_ms = 3600000

  labels = {
    env = "default"
  }
}