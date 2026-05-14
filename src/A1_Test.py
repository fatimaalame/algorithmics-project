import pandas as pd

from A1_Beginner import calculate_10k_goal_rate
from A1_Beginner import find_best_participant


# First, Id like to test with fake dataset to check if my algorithm works
test_data = {
    "participant_id": ["A", "A", "B", "B"],
    "ACTIVITY_steps": [12000, 5000, 11000, 13000],
}

df_test = pd.DataFrame(test_data)

rates = calculate_10k_goal_rate(df_test)
best_participant, best_rate = find_best_participant(rates)

print("Rates:", rates)
print("Best participant:", best_participant)
print("Best rate:", best_rate)

# Simple tests on the fake dataset
assert rates["A"] == 50.0  # Check if the rate of A is 50%
assert rates["B"] == 100.0  # Check if the rate of B is 100%
assert best_participant == "B"
assert best_rate == 100.0

# Now I test the same functions with the real dataset.
real_df = pd.read_csv("data/merged.csv")

real_rates = calculate_10k_goal_rate(real_df)
real_best_participant, real_best_rate = find_best_participant(real_rates)

print("\nReal dataset result:")
print("Best participant:", real_best_participant)
print("Best rate:", real_best_rate)

# Real dataset sanity checks
assert real_best_rate >= 0
assert real_best_rate <= 100

print("All beginner tests passed!")
 