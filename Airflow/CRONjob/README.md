# Run Airflow DAG to trigger data ingestion on the first day of every month

     # 0 0 1 * * airflow dags trigger data_ingestion_dag


To cancel the cron job, you would remove or comment out the corresponding line in the crontab file. (This is what I have done above)

After saving the crontab file, the cron job will no longer be scheduled.
