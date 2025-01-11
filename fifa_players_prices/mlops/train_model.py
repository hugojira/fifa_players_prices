# This code train a randon forest regressor from sklearn. Logs the hyperparameters and the trained model to mlflow
# it also pushes the run_id from mlflow so the next script score_model can use it

# Import the required libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import mlflow

def train_model(**kwargs):
    # Read the training data
    docker_data_path = '/opt/airflow/split_data/'
    X_train = pd.read_csv(docker_data_path + 'X_train.csv')
    y_train = pd.read_csv(docker_data_path + 'y_train.csv')
    # Reshape y_train for the random forest regressor
    y_train_reshaped = y_train.values.ravel()

    # Set the tracking URI:
    #  it must be http://NAME-OF-THE-MLFLOW-CONTAINER:port
    mlflow.set_tracking_uri("http://docker-mlflow-server-1:5000")

    # Start a run
    with mlflow.start_run():
       n_estimators = 30
       max_depth = 10

       mlflow.log_param("n_estimators", n_estimators)
       mlflow.log_param("max_depth", max_depth)
       
       # Create a Random Forest Regressor
       rf_regressor = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
       
       # Fit the model to the training data
       rf_regressor.fit(X_train, y_train_reshaped)
       
       # Log the model
       input_example = X_train.sample(n=1) # input example to infer the schema
       mlflow.sklearn.log_model(rf_regressor, "random_forest_model", input_example=input_example)

       # push the run id with XCOM so the scoring task can use it to load the model and score metrics
       run_id = mlflow.active_run().info.run_id
       # f4c96abec6fd41ce9ad2aaabdabbe605
    kwargs['ti'].xcom_push(key='mlflow_run_id', value=run_id)