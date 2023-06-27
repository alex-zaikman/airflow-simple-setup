from datetime import datetime, timedelta
from operators.postgres_table_import_from_s3_operator import ImportTableFromS3Operator
from airflow import DAG

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 9, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("load_from_s3", default_args=default_args, schedule_interval=timedelta(seconds=10))

t1 = ImportTableFromS3Operator(task_id="load_data",
                               table='s3test',
                               columns=['a', 'b', 'c', 'd', 'e'],
                               bucket='okapi-dev-test',
                               file_path='fs3.csv',
                               dag=dag)
