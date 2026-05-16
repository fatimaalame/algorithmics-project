import pandas as pd

from A2_Intermediate import top_k_days_baseline
from A2_Intermediate import top_k_days_improved


#First: test with a small fake dataset
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

print("Baseline result:")
print(baseline_result)

print("\nImproved result:")
print(improved_result)


#Simple fake dataset tests
expected_A = [("Thu", 15000), ("Tue", 12000), ("Sat", 11000)]
expected_B = [("Wed", 10000), ("Tue", 7000), ("Mon", 3000)]

assert baseline_result["A"] == expected_A
assert baseline_result["B"] == expected_B
assert improved_result["A"] == expected_A
assert improved_result["B"] == expected_B

#The two approaches should return the same result btw
assert baseline_result == improved_result

print("\nFake dataset tests passed.")


#Now I test with the real merged dataset
real_df = pd.read_csv("data/merged.csv")

real_baseline = top_k_days_baseline(real_df, k=5)
real_improved = top_k_days_improved(real_df, k=5)

#The baseline and improved version should return the same step counts
for participant in real_baseline:
    baseline_steps = []
    improved_steps = []

    for day in real_baseline[participant]:
        baseline_steps.append(day[1])

    for day in real_improved[participant]:
        improved_steps.append(day[1])

    assert baseline_steps == improved_steps

print("Real dataset check passed.")

print("\nExample result for participant 7359:")
print(real_improved[7359])