from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depend_on_past': False,
    'start_date': datetime(2020, 4, 13),
    'retries': 0

}

dag = DAG(dag_id='DAG-1', default_args=default_args, catchup=False, schedule_interval='@once')


start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end 


