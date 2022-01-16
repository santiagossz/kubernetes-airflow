from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from datetime import datetime

default_args = {
    'start_date': datetime.now(),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}


with DAG(dag_id='ks8_etl', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:
    
    
    ks8_load_data = KubernetesPodOperator(
                          image="amancevice/pandas",
                          cmds=["python","-c"],
                          arguments=["pd.read_csv('https://ifood-data-architect-test-source.s3-sa-east-1.amazonaws.com/consumer.csv.gz').to_csv('/opt/airflow/dags/data/consumer.csv',index=False)"],
                          task_id="ks8_load_data",
                          )


    ks8_read_data = KubernetesPodOperator(
                          image="python:3.8",
                          cmds=["python","-c"],
                          arguments=["print(pd.read_csv('/opt/airflow/dags/data/consumer.csv'))"],
                          task_id="ks8_read_data",
                          )


    ks8_load_data >> ks8_read_data 
        