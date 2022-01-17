# iFood Data Engineer Test

## 2st Case: Airflow

This is my proposed Airflow Orchestration for the [iFood Engineer Test](https://github.com/wiflore/ifood-data-engineering-test.git), to orchestrate a data pipeline using airflow inside a Kubernetes cluster, with a Kubernetes executor and running each task with  KubernetesPod Operator in order to download/store a csv file  and read/print its results.



## Solution

create a Kubernetes cluster with kind

`kind create cluster --config config/kind-config.yaml`

create namespace to have all airflow resources 

`kubectl create ns airflow`

airflow docker image w/ kubernetespod operator provider, and pandas

`santiagossz/ifood:airflow_dags` 


 helm chart of airflow to install the secheduler, database & web application independently inside Kubernetes cluster
 
 `helm repo add apache-airflow https://airflow.apache.org`

 Using the personlized [helm values](/config/ks8_values.yaml) to use the docker image to copy the dags and the requirements inside the cluster

 `helm install airflow apache-airflow/airflow -n airflow -f config/ks8_values.yaml --debug `

forward the port to load Airflow UI

`kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow`

Open your [localhost](http://localhost:8080/) with the credentials:

username `admin`
password `admin`

Inside the Airflow UI trigger the KubernetesPodOperator data pipeline dag to start the etl process

![Trigger ks8_dag](/assets/dag.png)