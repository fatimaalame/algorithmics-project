from A3_Advanced import convert_date

#Step 1: checking if the date format from the dataset works
converted_date = convert_date("06.07.21")

print(converted_date)

assert str(converted_date) == "2021-07-06"

print("Step 1 passed: date conversion works.")
