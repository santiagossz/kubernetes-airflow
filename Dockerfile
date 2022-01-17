FROM apache/airflow:2.2.3

COPY requirements.txt .

COPY /dags /opt/airflow/dags
 
RUN pip install -r requirements.txt