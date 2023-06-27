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

dag = DAG("sqldag_complex", default_args=default_args, schedule_interval=timedelta(seconds=10))

t1 = PostgresOperator(task_id="add_data1",
                      sql=f"INSERT INTO test.test_table(stamp, data) VALUES ('{str(datetime.now())}', 'add_data1')",
                      autocommit=True,
                      dag=dag)

t2 = PostgresOperator(task_id="add_data2",
                      sql=f"INSERT INTO test.test_table(stamp, data) VALUES ('{str(datetime.now())}', 'add_data2')",
                      autocommit=True,
                      dag=dag)
t3 = PostgresOperator(task_id="add_data3",
                      sql=f"INSERT INTO test.test_table(stamp, data) VALUES ('{str(datetime.now())}', 'add_data3')",
                      autocommit=True,
                      dag=dag)

t1 >> [t2, t3]
