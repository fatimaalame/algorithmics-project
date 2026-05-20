# Analysis 3: longest 10k-step streak

from datetime import datetime, timedelta

import pandas as pd


def convert_date(date_text):
    # Dates in the CSV are written like "06.07.21".
    # I convert them so Python can sort them correctly.
    return datetime.strptime(str(date_text), "%d.%m.%y").date()


def group_days_by_participant(data):
    # Put all days of the same participant together.
    participants = {}

    for row in data:
        participant_id = row["participant_id"]
        date_text = row["DATE"]
        steps_value = row["ACTIVITY_steps"]

        # Skip incomplete rows.
        if pd.isna(participant_id) or pd.isna(date_text) or pd.isna(steps_value):
            continue

        date = convert_date(date_text)
        steps = int(float(steps_value))

        if participant_id not in participants:
            participants[participant_id] = []

        participants[participant_id].append((date, steps))

    return participants


def sort_days_by_date(days):
    # For A3, I need the days in chronological order.
    # I use Python sorted() to make the streak logic clear.
    return sorted(days, key=lambda day: day[0])


def longest_10k_streak_for_participant(days):
    # Find the longest consecutive streak with at least 10k steps for one participant.
    # DP-style idea: current_streak depends on the previous day.
    # I only keep the current streak and the best streak found so far.
    sorted_days = sort_days_by_date(days)

    longest_streak = 0
    current_streak = 0
    previous_active_date = None

    for date, steps in sorted_days:
        if steps >= 10000:
            # If this is the first active day, start a new streak.
            if previous_active_date is None:
                current_streak = 1

            # If this active day is the day after the previous active day, continue.
            elif date == previous_active_date + timedelta(days=1):
                current_streak = current_streak + 1

            # Otherwise, the active days are not consecutive, so restart.
            else:
                current_streak = 1

            previous_active_date = date

            if current_streak > longest_streak:
                longest_streak = current_streak

        else:
            # A day below 10k breaks the streak.
            current_streak = 0
            previous_active_date = None

    return longest_streak


def longest_10k_streak_all_participants(data):
    # Apply the longest streak function to every participant.
    participants = group_days_by_participant(data)
    result = {}

    for participant_id in participants:
        days = participants[participant_id]
        result[participant_id] = longest_10k_streak_for_participant(days)

    return result




############# TESTS ###########


if __name__ == "__main__":
    # Tests for A3

    # Step 1: checking if the date format from the dataset works
    converted_date = convert_date("06.07.21")

    print(converted_date)

    assert str(converted_date) == "2021-07-06"

    print("Step 1 passed: date conversion works.")


    # Step 2: checking if the merged CSV file can be loaded
    df = pd.read_csv("data/merged.csv")

    print("\nDataset loaded.")
    print("Columns:", df.columns.tolist())

    assert "DATE" in df.columns
    assert "ACTIVITY_steps" in df.columns
    assert "participant_id" in df.columns

    print("Step 2 passed: dataset loading works")


    # Step 3: checking if rows can be grouped by participant
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


    # Step 4: fake dataset test for longest 10k streak
    fake_data = [
        {"participant_id": "A", "DATE": "01.01.21", "ACTIVITY_steps": "12000"},
        {"participant_id": "A", "DATE": "02.01.21", "ACTIVITY_steps": "13000"},
        {"participant_id": "A", "DATE": "03.01.21", "ACTIVITY_steps": "9000"},
        {"participant_id": "A", "DATE": "04.01.21", "ACTIVITY_steps": "15000"},
        {"participant_id": "A", "DATE": "05.01.21", "ACTIVITY_steps": "16000"},
        {"participant_id": "A", "DATE": "06.01.21", "ACTIVITY_steps": "17000"},
        {"participant_id": "B", "DATE": "01.01.21", "ACTIVITY_steps": "5000"},
        {"participant_id": "B", "DATE": "02.01.21", "ACTIVITY_steps": "11000"},
        {"participant_id": "B", "DATE": "03.01.21", "ACTIVITY_steps": "12000"},
    ]

    fake_result = longest_10k_streak_all_participants(fake_data)

    print("\nFake streak result:")
    print(fake_result)

    assert fake_result["A"] == 3
    assert fake_result["B"] == 2

    # Extra edge case: no active days.
    fake_no_active = [
        {"participant_id": "C", "DATE": "01.01.21", "ACTIVITY_steps": "4000"},
        {"participant_id": "C", "DATE": "02.01.21", "ACTIVITY_steps": "7000"},
    ]
    no_active_result = longest_10k_streak_all_participants(fake_no_active)
    assert no_active_result["C"] == 0

    # Extra edge case: missing calendar day breaks the streak.
    fake_missing_day = [
        {"participant_id": "D", "DATE": "01.01.21", "ACTIVITY_steps": "12000"},
        {"participant_id": "D", "DATE": "03.01.21", "ACTIVITY_steps": "13000"},
    ]
    missing_day_result = longest_10k_streak_all_participants(fake_missing_day)
    assert missing_day_result["D"] == 1

    print("Step 4 passed: fake streak test works")


    # Step 5: real dataset check for longest streaks
    real_result = longest_10k_streak_all_participants(data)

    print("\nLongest 10k streaks on real dataset:")
    print(real_result)

    best_participant = None
    best_streak = -1

    for participant_id in real_result:
        if real_result[participant_id] > best_streak:
            best_streak = real_result[participant_id]
            best_participant = participant_id

    print("\nBest participant for longest 10k streak:")
    print(best_participant, best_streak)

    assert best_participant is not None
    assert best_streak >= 0

    print("Step 5 passed: real dataset streak check works")

    # Intentionally failing test.
    # To see it fail, uncomment the line below.
    # assert fake_result["A"] == 2, "Intentional failing test: A's streak should be 3."