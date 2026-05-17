import os
import sys

from A3_Advanced import convert_date, group_days_by_participant

#Add the src folder so Python can find data_loader.py
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, "src")
sys.path.append(src_path)

from data_loader import load_data


#Step 1: checking if the date format from the dataset works
converted_date = convert_date("06.07.21")

print(converted_date)

assert str(converted_date) == "2021-07-06"

print("Step 1 passed: date conversion works.")


#Step 2: checking if the merged CSV file can be loaded
data_path = os.path.join(project_root, "data", "merged.csv")

df = load_data(data_path)

print("\nFirst rows of the dataset:")
print(df.head())

print("\nDataset columns:")
print(df.columns)

assert "DATE" in df.columns
assert "ACTIVITY_steps" in df.columns
assert "participant_id" in df.columns

print("Step 2 passed: dataset loading works")


#Step 3: checking if rows can be grouped by participant
data = df.to_dict(orient="records")
participants = group_days_by_participant(data)

print("\nNumber of participants:")
print(len(participants))

first_participant = list(participants.keys())[0]

print("\nFirst participant id:")
print(first_participant)

print("\nFirst participant first 3 days:")
print(participants[first_participant][:3])

assert len(participants) > 0
assert len(participants[first_participant]) > 0

print("Step 3 passed: grouping by participant works")