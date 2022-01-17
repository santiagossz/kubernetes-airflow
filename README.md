# iFood Data Engineer Test

## 2st Case: Airflow

This is my proposed Airflow Orchestration for the [iFood Engineer Test](https://github.com/wiflore/ifood-data-engineering-test.git), to create KubernetesPod task
in a Kubernetes Executor to download/store a file and read/print its results



## Solution

create a Kubernetes cluster with kind

`kind create cluster --config config/kind-config.yaml`

create namespace to have all airflow resources 

`kubectl create ns airflow`

airflow docker image w/ kubernetespod operator provider, and pandas

`santiagossz/ifood:airflow_dags` 

**values_ssh.yaml** have all the helm chart values, connection to docker airflow image && pods to run airflow with KubernetesExecutor 
 helm chart airflow install inside Kubernetes cluster
 
 `helm repo add apache-airflow https://airflow.apache.org`

 `helm install airflow apache-airflow/airflow -n airflow -f config/ks8_values.yaml --debug `

forward the port to have Airflow UI

`kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow`


Trigger the KubernetesPodOperator data pipeline dag to complete the etl process

![Trigger ks8_dag](/../dag.png)