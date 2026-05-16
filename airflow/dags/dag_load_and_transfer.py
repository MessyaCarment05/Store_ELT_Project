from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
import subprocess

default_args = {
    'owner': 'Messy',
    'depends_on_past': False
}

def dump_load_to_destinationdb():
    script_path = '/opt/airflow/elt_script/dump_and_load_data.py'
    result=subprocess.run(['python', script_path], capture_output=True, text=True)

    if result.returncode!=0:
        raise Exception(f"Script failed with error: {result.stderr}")
    else:
        print(result.stdout)

dag = DAG(
    "dag_load_and_transfer",
    default_args=default_args,
    start_date=datetime(2026,5,6),
    catchup = False,
    schedule_interval = '0 1 * * 0'
)

task_load_and_transfer_data=PythonOperator(
    task_id = "load_data_to_destinationdb",
    python_callable=dump_load_to_destinationdb,
    dag=dag
)

task_load_and_transfer_data