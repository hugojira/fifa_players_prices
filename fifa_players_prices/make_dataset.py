# Script to make the raw dataset
# It consists of 2 funcions:
# 1.- Download the csv files from Kaggle into "data/raw"
# 2.- Select only the csv file "male_players.csv" and delete the other ones.

# Libraries
import os
import kaggle

# Download dataset
def download_kaggle_dataset(dataset, destination_folder="data/raw"):
    """
    Downloads a dataset from Kaggle to a specified folder.

    Args:
        dataset (str): The name of the dataset on Kaggle.
        destination_folder (str, optional): The full path of the destination folder. Defaults to "data/raw".
    """

    # Check if the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Check if there are CSV files in the folder
    csv_files = [file for file in os.listdir(destination_folder) if file.endswith('.csv')]
    if not csv_files:
        # Download the dataset if there are no CSV files
        print(f"Downloading dataset {dataset} to {destination_folder}")
        kaggle.api.dataset_download_files(dataset, path=destination_folder, unzip=True)
    else:
        print(f"CSV files already exist in {destination_folder}. Dataset will not be downloaded.")

# Keep the selected CSV file
def keep_only_selected_csv(directory, selected_csv):
  """
  Keeps only the specified CSV file in the given directory 
  and deletes all other CSV files.

  Args:
    directory (str): Path to the directory containing the CSV files.
    selected_csv (str): Name of the CSV file to keep.
  """

  csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

  if not csv_files:
    print(f"No CSV files found in {directory}")
    return

  # Keep only the selected_csv file
  for file in csv_files:
    if file != selected_csv:
      file_path = os.path.join(directory, file)
      os.remove(file_path)
      print(f"Deleted: {file}")
  print(f"Kept: {selected_csv}")

def main():
  dataset = "stefanoleone992/ea-sports-fc-24-complete-player-dataset"  # Reemplaza con el nombre de tu dataset
  directory = "/Users/hugo/PyProjects/fifa-players-prices/fifa_players_prices/data/raw"
  selected_file = "male_players.csv"

  download_kaggle_dataset(dataset, directory)
  keep_only_selected_csv(directory, selected_file)

if __name__ == "__main__":
  main()
