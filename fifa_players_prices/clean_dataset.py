# This script takes the raw dataset as input, remove the missing values, remove columns that will not be used
# and applies log transformation into the target variable value

# Libraries
import pandas as pd
import numpy as np

def read_dataset(raw_path):
    df_raw = pd.read_csv(raw_path)
    return df_raw

def select_columns(df, columns_list):
    # Accept a list of the columns to select and the df
    return df[columns_list]

def remove_missing_values(df):
    # Remove the dato from Goalkeepers and all the rows with missing values
    df_nonan = df[df.player_positions != "GK"].dropna(axis=0)
    return df_nonan

def log_value(df):
    # applies the log to the value "value_eur" of the "df" dataframe
    # and creates the column "value_eur_log"
    # that is, it aplplies the log to the values of the players in order
    # to have a smoother distribution
    df["value_eur_log"] = np.log(df["value_eur"])
    return df

def test_steps(df):
    # make sure there are no missing values, and the columns selected are the correct ones

    # no missing values
    assert df.isnull().any(axis=1).any() == False, "there are missing values in the data"

    # make sure all the columns are the correct ones
    required_columns = ['player_id', 'fifa_version', 'fifa_update', 'update_as_of',
       'short_name', 'long_name', 'potential', 'value_eur', 'age', 'height_cm',
       'weak_foot', 'international_reputation', 'club_position',
       'player_positions', 'pace', 'shooting', 'passing', 'dribbling',
       'defending', 'physic', 'value_eur_log']
    
    missing_columns = set(required_columns) - set(df.columns)
    assert len(missing_columns) == 0, f"Missing required columns: {missing_columns}"

def save_dataset(df, clean_data_path):
    df.to_csv(clean_data_path, index=False) 
    print(f"the final dataset has been saved at: {clean_data_path}")

def main():
    # declaring needed parameters
    raw_path = "../data/raw/male_players.csv"
    columns_list = ['player_id', 'fifa_version', 'fifa_update', 'update_as_of',
       'short_name', 'long_name', 'potential', 'value_eur', 'age', 'height_cm',
       'weak_foot', 'international_reputation', 'club_position',
       'player_positions', 'pace', 'shooting', 'passing', 'dribbling',
       'defending', 'physic']
    clean_data_path = "/Users/hugo/PyProjects/fifa-players-prices/fifa_players_prices/data/processed/final_data.csv"

    # steps to clean de dataset
    df = read_dataset(raw_path)
    df = select_columns(df, columns_list)
    df = remove_missing_values(df)
    df = log_value(df)

    test_steps(df)
    save_dataset(df, clean_data_path)

if __name__ == "__main__":
  main()
