# FIFA players prices

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

And end-to-end ML project to predict the prices of football players using data from FIFA (FC Sports) videogames. The goal is to showcase the MLOps lifecycle using Microsoft Azure.

The data was taken from Kaggle, the FIFA videogame data from 2015 to 2023.

This project uses Docker to define Airflow and MLFlow services, in order to use a DAG to prepare the data, train and score the model, while logging metricst and the artifacts. The main python code is executed in Docker, so some volumes are define in order to save the processed data and models.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         fifa_players_prices and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
|
├── Docker             <- Docker files to build the airflow and mlops services
|
├── airflow            <- airflow directory, where dags are stored
|
├── mlflow-data        <- mlflow directory, where the database and models are stored
│
└── fifa_players_prices   <- Source code for use in this project.
    │
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── make_dataset.py          <- Scripts to download data from kaggle
    │
    ├── clean_dataset.py          <- Code to clean the data
    │
    ├── mlops                
    │   ├── prepare_data.py 
    │   ├── train_model.py          <- Code to run train the model        
    │   └── score_model.py          <- Code to evaluate the model
    │
    └── plots.py                <- Code to create visualizations
```

--------

## How to set up Airflow and Docker

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

References:

[https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

[https://medium.com/@dast04/running-airflow-with-docker-compose-2023-for-machine-learning-a78eeadc00cd](https://medium.com/@dast04/running-airflow-with-docker-compose-2023-for-machine-learning-a78eeadc00cd)

