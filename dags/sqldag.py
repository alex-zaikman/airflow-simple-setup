from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta


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

dag = DAG("sqldag", default_args=default_args, schedule_interval=timedelta(seconds=10))

t1 = PostgresOperator(task_id="add_data1",
                      sql=f"INSERT INTO test.test_table(stamp, data) VALUES ('{str(datetime.now())}', 'hello')",
                      autocommit=True,
                      dag=dag)

