# Airflow and MLFlow

Airflow image taken from the [official airflow site](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html). Follow those steps in order to configure the containers.

Just commented the lines in the docker compose file that are not needed in this project and added the MLFlow service. The Airflow and MLFlow containers communicate using the default network.

See the [final docker compose file](./docker-compose.yaml).

## How to use the docker containers

1. First, Docker and docker-compose need to be installed.
2. Go to the folder ./docker and run the following commands

- **Run airflow/mlflow services**

docker-compose up airflow-init

docker-compose up -d

- **Stop the containers and remove volumes (local files are kept)**

docker compose down --volumes --remove-orphans

### To access the webservices in the ports
**Airflow:** http://localhost:8080/

**MLFlow:** http://localhost:5001/

## MLFlow Tracking URI

The scripts for logging to MLFLow are run with the Airflow container, so the tracking URI must be in the following format

mlflow.set_tracking_uri("http://NAME-OF-THE-MLFLOW-CONTAINER:PORT-OF-THE-CONTAINER")

**Example:**

mlflow.set_tracking_uri("http://docker-mlflow-server-1:5000")

## Volumes

Some volumes were defined in order to save the required files locally.

### Airflow volumes

Considerando AIRFLOW_PROJ_DIR=../airflow/

- ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
- ${AIRFLOW_PROJ_DIR:-.}/logs:/opt/airflow/logs
- ${AIRFLOW_PROJ_DIR:-.}/config:/opt/airflow/config
- ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/plugins
- /Users/hugo/PyProjects/fifa-players-prices/fifa_players_prices/data/processed:/opt/airflow/split_data
- /Users/hugo/PyProjects/fifa-players-prices/fifa_players_prices/fifa_players_prices:/opt/airflow/src

### MLflow volume

- ../mlflow-data:/mlflow

## References

Useful links that I used as reference 

- [https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- [https://medium.com/@dast04/running-airflow-with-docker-compose-2023-for-machine-learning-a78eeadc00cd](https://medium.com/@dast04/running-airflow-with-docker-compose-2023-for-machine-learning-a78eeadc00cd)

