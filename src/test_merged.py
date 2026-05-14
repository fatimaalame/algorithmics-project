# Import to read the merged CSV file
import pandas as pd


def main():
    # Load the merged dataset from the data folder
    df = pd.read_csv("data/merged.csv")

    # Print basic information to understand the dataset
    print("Dataset loaded successfully.")
    print("Rows:", len(df))
    print("Columns:")
    print(df.columns.tolist())

    # Print the first rows to see what the data looks like
    print("\nFirst 5 rows:")
    print(df.head())


if __name__ == "__main__":
    main()

