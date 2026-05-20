# Analysis 2: Top 5 active days per participant

import pandas as pd


# df y3ne = receive the CSV
def group_days_by_participant(df):
    # This empty dictionary (then store something) where key=idparticip and value=list de jours+ses pas
    days_by_participant = {}

    # We go through the dataset row by row 
    for index, row in df.iterrows():
        participant = row["participant_id"]
        date = row["DATE"]
        steps = row["ACTIVITY_steps"]

        #Skip missing participant, date, or step values
        if pd.isna(participant) or pd.isna(date) or pd.isna(steps):
            continue

        #if first time see this participant then create an empty list
        if participant not in days_by_participant:
            days_by_participant[participant] = []

        #add this day to the participant's list
        days_by_participant[participant].append((date, steps)) #("06.07.21, 12000")-> tuple btw

    return days_by_participant


def insertion_sort_days_by_steps(days):
    # A copy bcs we dont wanna change the original list
    sorted_days = days.copy()

    # Start at index 1 because the 1st elem. alone is already sorted
    for current_index in range(1, len(sorted_days)):
        day_to_insert = sorted_days[current_index]
        scan_index = current_index - 1 #compare with the left number

        # We shift smaller step counts to the right
        # We want descending order, so bigger step counts come first 
        while scan_index >= 0 and sorted_days[scan_index][1] < day_to_insert[1]:
            sorted_days[scan_index + 1] = sorted_days[scan_index]
            scan_index = scan_index - 1

        # We insert the day at the correct position.
        sorted_days[scan_index + 1] = day_to_insert

    return sorted_days


def top_k_days_baseline(df, k=5):
    # Awalan, group the days by participant
    days_by_participant = group_days_by_participant(df)

    # Dictionary will store the top k days for each participant
    top_days = {}

    # Go through every participant 1 by 1
    for participant in days_by_participant:
        days = days_by_participant[participant]

        # Baseline: sort all days, even if we only need the first k.
        sorted_days = insertion_sort_days_by_steps(days)

        # Keep only the first k days.
        top_days[participant] = sorted_days[:k]

    return top_days


def find_smallest_day_index(days):
    # Find the index of the day with the smallest number of steps
    smallest_index = 0

    for i in range(1, len(days)):
        if days[i][1] < days[smallest_index][1]:
            smallest_index = i

    return smallest_index


def insert_day_descending(top_days, new_day):
    # Insert a new day in descending order by step count
    # This inserts a day into a small sorted list btw
    top_days.append(new_day)

    current_index = len(top_days) - 1
    day_to_insert = top_days[current_index]
    scan_index = current_index - 1

    while scan_index >= 0 and top_days[scan_index][1] < day_to_insert[1]:
        top_days[scan_index + 1] = top_days[scan_index]
        scan_index = scan_index - 1

    top_days[scan_index + 1] = day_to_insert

    return top_days


def top_k_days_improved(df, k=5):
    # First, group the days by participant
    days_by_participant = group_days_by_participant(df)

    # This dictionary will store the top k days for each participant
    result = {}

    # Go through every participant one by one
    for participant in days_by_participant:
        days = days_by_participant[participant]
        current_top = [] #best 5 dayz for one person // key variable

        # Scan the days without sorting the whole list
        for day in days:
            if len(current_top) < k:
                current_top = insert_day_descending(current_top, day)
            else:
                smallest_index = find_smallest_day_index(current_top)

                #If the new day is better than the smallest top day -> replace it
                if day[1] > current_top[smallest_index][1]:
                    current_top.pop(smallest_index)
                    current_top = insert_day_descending(current_top, day)

        result[participant] = current_top

    return result


def top_k_days_builtin(df, k=5):
    # This version uses Python's built-in sorted()
    # I use it to compare my own sorting algorithm with a built-in function
    days_by_participant = group_days_by_participant(df)

    result = {}

    for participant in days_by_participant:
        days = days_by_participant[participant]

        sorted_days = sorted(days, key=lambda day: day[1], reverse=True)

        result[participant] = sorted_days[:k]

    return result



######### TESTS #############


def run_fake_dataset_tests():
    # First: test with a small fake dataset
    test_data = {
        "participant_id": ["A", "A", "A", "A", "A", "A", "B", "B", "B"],
        "DATE": [
            "Mon", "Tue", "Wed", "Thu", "Fri", "Sat",
            "Mon", "Tue", "Wed"
        ],
        "ACTIVITY_steps": [
            8000, 12000, 6000, 15000, 9000, 11000,
            3000, 7000, 10000
        ],
    }

    df_test = pd.DataFrame(test_data)

    baseline_result = top_k_days_baseline(df_test, k=3)
    improved_result = top_k_days_improved(df_test, k=3)
    builtin_result = top_k_days_builtin(df_test, k=3)

    print("Baseline result:")
    print(baseline_result)

    print("\nImproved result:")
    print(improved_result)
    print("\nBuilt-in sorted result:")
    print(builtin_result)

    # Simple fake dataset tests
    expected_A = [("Thu", 15000), ("Tue", 12000), ("Sat", 11000)]
    expected_B = [("Wed", 10000), ("Tue", 7000), ("Mon", 3000)]

    assert baseline_result["A"] == expected_A
    assert baseline_result["B"] == expected_B
    assert improved_result["A"] == expected_A
    assert improved_result["B"] == expected_B
    assert builtin_result["A"] == expected_A
    assert builtin_result["B"] == expected_B

    # The three approaches should return the same result btw
    assert baseline_result == improved_result
    assert baseline_result == builtin_result

    # Edge case: participant with fewer days than k
    test_data_small = {
        "participant_id": ["C", "C"],
        "DATE": ["Mon", "Tue"],
        "ACTIVITY_steps": [5000, 8000],
    }
    df_small = pd.DataFrame(test_data_small)
    result_small = top_k_days_improved(df_small, k=5)
    # C only has 2 days, so we expect 2 results max (not 5)
    assert len(result_small["C"]) == 2
    print("Edge case test passed (fewer days than k).")

    print("\nFake dataset tests passed.")


def run_real_dataset_check():
    # Now I test with the real merged dataset
    real_df = pd.read_csv("data/merged.csv")

    real_baseline = top_k_days_baseline(real_df, k=5)
    real_improved = top_k_days_improved(real_df, k=5)
    real_builtin = top_k_days_builtin(real_df, k=5)

    # The baseline and improved version should return the same step counts
    for participant in real_baseline:
        baseline_steps = []
        improved_steps = []
        builtin_steps = []

        for day in real_baseline[participant]:
            baseline_steps.append(day[1])

        for day in real_improved[participant]:
            improved_steps.append(day[1])

        for day in real_builtin[participant]:
            builtin_steps.append(day[1])

        # We only compare step counts, not dates
        # because ties in steps can produce different but equally valid orderings
        assert baseline_steps == improved_steps
        assert baseline_steps == builtin_steps

    print("Real dataset check passed.")

    print("\nExample result for participant 7359:")
    print(real_improved[7359])
    print("\n")


def run_builtin_sorted_check():
    # Small direct check with only a list of days
    # Baseline = my insertion sort
    # Built-in = Python sorted()
    test_days = [("Mon", 3000), ("Tue", 12000), ("Wed", 7000)]

    baseline_result = insertion_sort_days_by_steps(test_days)
    builtin_result = sorted(test_days, key=lambda day: day[1], reverse=True)
    
    assert baseline_result == builtin_result

    print("Built-in sorted comparison passed.")


def run_failing_test():
    # This test is intentionally wrong !
    # The algorithm sorts from highest steps to lowest steps,
    # but here I pretend that the smallest value should come first
    test_days = [("Mon", 3000), ("Tue", 12000), ("Wed", 7000)]

    result = insertion_sort_days_by_steps(test_days)

    assert result == [
        ("Mon", 3000),
        ("Wed", 7000),
        ("Tue", 12000)
    ], "Failing test: this is wrong because the algorithm sorts in descending order."


if __name__ == "__main__":
    run_fake_dataset_tests()
    run_real_dataset_check()
    run_builtin_sorted_check()
    # run_failing_test()
    # I put it in a comment, you just have to remove it and it'll give you the AssertionError :)