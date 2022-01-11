from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
import pandas as pd

from datetime import datetime

default_args = {
    'start_date': datetime.now(),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}

def process(p1):
    print(p1)
    return 'done'

with DAG(dag_id='etl', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:
    
    # Tasks dynamically generated 
    tasks = [BashOperator(task_id='task_{0}'.format(t), bash_command='sleep 5'.format(t)) for t in range(1, 4)]
    download_store = KubernetesPodOperator(namespace='default',
                          image="python:3.8",
                          cmds=["python","-c"],
                          arguments=["pd.read_csv('https://ifood-data-architect-test-source.s3-sa-east-1.amazonaws.com/consumer.csv.gz',header=True).to_csv('consumer.csv',index=False)"],
                          labels={"foo": "bar"},
                          name="download_store",
                          task_id="download_store",
                          get_logs=True,
                          dag=dag
                          )


       read_print = KubernetesPodOperator(namespace='default',
                          image="python:3.8",
                          cmds=["python","-c"],
                          arguments=["print(pd.read_csv('example.csv',header=True))"],
                          labels={"foo": "bar"},
                          name="read_print",
                          task_id="read_print",
                          get_logs=True,
                          dag=dag
                          )


    download_store >> read_print 
        