# This script created a functions that reads the processed data and splits it in training and testing, X and y
# so the model in the training script can load it

# Importing the required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def prepare_data():
    #local_path = '/Users/hugo/PyProjects/fifa-players-prices/fifa_players_prices/data/processed/'
    docker_path = '/opt/airflow/split_data/'
    df = pd.read_csv(docker_path + 'final_data.csv')
    assert df.isnull().any(axis=1).any() == False, "there are missing values in the data, prepare_data task failed"
    
    # features
    features = ['age', 'height_cm', 'weak_foot', 'international_reputation', 'potential',
            'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
    target_variable = ['value_eur_log']

    # Converting also the height_cm and potential to a float
    df[['height_cm', 'potential']] = df[['height_cm', 'potential']].astype(float) 
    
    # The features X and the target variable y
    X = df[features]
    y = df[target_variable]

    # ----- split data -----
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 

    # ---- Export the data to the PROCESSED folder ----
    #local_save_path = '/Users/hugo/PyProjects/fifa-players-prices/fifa_players_prices/data/processed/'
    docker_save_path = '/opt/airflow/split_data/'

    X_train.to_csv(docker_save_path + 'X_train.csv', index=False) 
    X_test.to_csv(docker_save_path + 'X_test.csv', index=False)
    y_train.to_csv(docker_save_path + 'y_train.csv', index=False)
    y_test.to_csv(docker_save_path + 'y_test.csv', index=False) 

prepare_data()