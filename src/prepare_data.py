## lire tous les CSV dans researchdata/
## ajouter une colonne participant_id
#fusionner tout
## sauvegarder le résultat dans data/merged.csv
##afficher le nombre total de lignes
## afficher le nombre de participants

# prepare_data.py
# Prepare the smartwatch dataset by merging all participant CSV files.

import os
import pandas as pd


def load_all_participants(input_folder: str) -> pd.DataFrame:
    """
    Load all participant CSV files from the input folder.

    A participant_id column is added using the filename without '.csv'.

    Parameters
    ----------
    input_folder : str
        Path to the folder containing participant CSV files.

    Returns
    -------
    pd.DataFrame
        One merged DataFrame containing all participants.
    """
    dataframes = []

    # Go through all files in the researchdata folder.
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)

            # Load one participant file.
            df = pd.read_csv(file_path)

            # Use the filename as participant ID.
            participant_id = filename.replace(".csv", "")
            df["participant_id"] = participant_id

            # Store this participant data.
            dataframes.append(df)

    # Merge all participant DataFrames into one.
    merged = pd.concat(dataframes, ignore_index=True)
    return merged


def save_merged_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the merged DataFrame as a CSV file.
    """
    df.to_csv(output_path, index=False)


def main():
    input_folder = "researchdata"
    output_path = "data/merged.csv"

    merged = load_all_participants(input_folder)
    save_merged_data(merged, output_path)

    print("Merged dataset created successfully.")
    print(f"Total rows: {len(merged):,}")
    print(f"Participants: {merged['participant_id'].nunique()}")
    print(f"Columns: {merged.columns.tolist()}")


if __name__ == "__main__":
    main()