FROM apache/airflow:2.1.0

COPY requirements.txt .

# COPY ./dags/ \${AIRFLOW_HOME}/dags/

 
RUN pip install -r requirements.txt