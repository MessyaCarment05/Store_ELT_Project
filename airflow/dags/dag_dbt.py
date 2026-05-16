from airflow import DAG
from datetime import datetime
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

default_args = {
    'owner': 'Messy',
    'depends_on_past': False
}



dag = DAG(
    "dag_dbt_v05",
    default_args=default_args,
    start_date=datetime(2026,5,6),
    catchup = False,
    schedule_interval = None
)

task_transforms_dbt = DockerOperator(
    task_id='transformation_using_dbt',
    image='ghcr.io/dbt-labs/dbt-postgres:1.4.7',
    command=[
        "run",
        "--profiles-dir",
        "/root",
        "--project-dir",
        "/dbt",
        "--full-refresh"
    ],
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mount_tmp_dir=False,
    mounts=[
        Mount(source='C:/Data Engineering Course/Project/Project_DE_ELT/postgres_transformations',
              target='/dbt', type='bind'),
        Mount(source='C:/Users/Messya Carment/.dbt', target='/root', type='bind'),
    ],
    dag=dag
)