# data_loader.py
# Utility functions to load and inspect the smartwatch dataset.

import pandas as pd


def load_participant_data(file_path: str) -> pd.DataFrame:
    """
    Load one participant CSV file.

    Parameters
    ----------
    file_path : str
        Path to the participant CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded participant data.
    """
    df = pd.read_csv(file_path)
    return df


def print_basic_statistics(df: pd.DataFrame) -> None:
    """
    Print basic information about the dataset.

    This is used to understand the structure of the data before
    writing algorithms.
    """
    print("Shape:")
    print(df.shape)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nBasic statistics:")
    print(df.describe())

    print("\nMissing values:")
    print(df.isnull().sum())


def main():
    # Load one participant file to inspect the dataset.
    file_path = "researchdata/1487.csv"
    df = load_participant_data(file_path)

    # Print the information required before starting the analyses.
    print_basic_statistics(df)


if __name__ == "__main__":
    main()


# Alias for compatibility
load_data = load_participant_data    