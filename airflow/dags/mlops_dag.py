# MLOps DAG to run prep data, train model and score model in airflow docker container

# Import the required libraries
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

# Python modules to be run as DAG tasks
sys.path.append('/opt/airflow/src/mlops/')

from prepare_data import prepare_data 
from train_model import train_model 
from score_model import score_model

with DAG(
    dag_id='mlops_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    prepare_data_task = PythonOperator(
        task_id='prepare_data_task',
        python_callable=prepare_data,
        dag=dag
    )

    train_model_task = PythonOperator(
        task_id='train_model_task',
        python_callable=train_model,
        provide_context=True ,
        dag=dag
    )

    score_model_task = PythonOperator(
        task_id='score_model_task',
        python_callable=score_model,
        provide_context=True, 
        dag=dag
    )

    prepare_data_task >> train_model_task >> score_model_task

