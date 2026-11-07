from datetime import datetime
from airflow.sdk import dag, task

@dag(
    dag_id="hello_world",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def hello_world():
    @task
    def dis_bonjour():
        print("Bonjour depuis Airflow !")

    dis_bonjour()

hello_world()