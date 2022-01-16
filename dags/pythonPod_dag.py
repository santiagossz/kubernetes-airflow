import pandas as pd
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator




default_args = {
    'start_date': datetime.now(),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}

def _load_data():
    pd.read_csv('https://ifood-data-architect-test-source.s3-sa-east-1.amazonaws.com/consumer.csv.gz').to_csv('consumer.csv',index=False)
    print('Successfull download and storage of file') 

def _read_data():
    df=pd.read_csv('consumer.csv')
    print(df) 

with DAG(dag_id='etl', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:

    load_data= PythonOperator(
        task_id='load_data',
        python_callable=_load_data
    )

    read_data= PythonOperator(
    task_id='read_data',
    python_callable=_read_data
    )

    load_data >> read_data