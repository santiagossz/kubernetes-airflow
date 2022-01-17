from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator




default_args = {
    'start_date': datetime.now(),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}

def print_test():
    print('hola')
    return 'hola'



with DAG(dag_id='test', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:

    test= PythonOperator(
        task_id='load_data',
        python_callable=print_test
    )

    test 