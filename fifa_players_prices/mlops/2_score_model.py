# Script to log the trained model, compute scoring metrics and log it to mlflow

# Import the required libraries
import pandas as pd
import numpy as np
import mlflow
from sklearn.metrics import r2_score, mean_squared_error

def score_model():
    # Import the testing data
    docker_data_path = '/opt/airflow/split_data/'
    X_test = pd.read_csv(docker_data_path + 'X_test.csv')
    y_test = pd.read_csv(docker_data_path + 'y_test.csv')

     #ti = kwargs['ti'] 
    #run_id = ti.xcom_pull(task_ids='train_model_task', key='mlflow_run_id')
    run_id = 'f4c96abec6fd41ce9ad2aaabdabbe605'
    mlflow.set_tracking_uri("http://docker-mlflow-server-1:5000")

    # Load the model using the retrieved run ID
    loaded_model = mlflow.sklearn.load_model(f"runs:/{run_id}/random_forest_model") 

    # Make predictions
    y_pred = loaded_model.predict(X_test)

    # Calculate metrics
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    # Log metrics to the existing run
    with mlflow.start_run(run_id=run_id):
        mlflow.log_metric("R2_score", r2)
        mlflow.log_metric("MSE", mse)

score_model()