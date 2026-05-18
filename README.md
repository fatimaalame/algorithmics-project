# AA Project

## Student: 
Fatima Alame (22-836-563)

## Project context
I'm working with real smartwatch data (provided by the uni) and using Python to explore daily activity patterns. The goal is not only to read the dataset, but also to apply the algorithmic ideas we got in class to a concrete way. I focus on writing simple functions, using loops and dictionaries, testing my code, and explaining why each algorithm made sense to me.


# Analysis 1: 10k steps goal achievement %

| Field | My answer |
|---|---|
| Problem I want to solve | Which participant reaches the 10k step goal most consistently? |
| Algorithm I will use | I use a linear scan through all the rows of the dataset. For each participant, I count the total number of recorded days and the number of days where they reached at least 10k steps. Then I calculate the success rate for each participant and scan the results to find the highest rate. |
| Why this algorithm is appropriate | This is a simple counting problem. Each row only needs to be checked once, so a linear scan is enough I guess. Dictionaries are useful because each participant can be stored as a key, with their counters as values. I chose a percentage instead of only counting days because participants may not all have the same number of recorded days (so that'd be cheating for some participants). |
| Expected time complexity | O(n + p), usually simplified to O(n), where n = nb of rows and p = nb of participants. |
| Expected space complexity | O(p), because the algorithm stores counters and rates for each participant. |
| How I tested | I tested the function on a small fake dataset where the expected result can be calculated by hand but I also tested it on the real merged dataset and checked that the final percentage is between 0 and 100. |
| Python file | Analysis/A1_Beginner.py |

### Result

The participant with the highest 10k step goal achievement rate is participant 7359, with a success rate of 94.83%.


# Analysis 2: Top 5 active days per participant

| Field | My answer |
|---|---|
| Problem I want to solve | What are the 5 most active days for each participant, based on the number of steps? |
| Algorithm I will use | First, I group the days by participant with a dictionary. The participant id is the key, and the value is a list of days with the date and the step count. Then, for each participant, I sort the days by steps in descending order and keep the first 5 days. For the baseline, I use insertion sort because we saw it in class and it is easy to follow. |
| Why this algorithm is appropriate | I need to separate the data by participant first, so a dictionary makes sense. Then I need to order the days from the most active to the least active. Insertion sort is not the fastest option, but it is simple and clear for a first version. The weak point is that it sorts all the days, even though I only need the top 5. |
| Expected time complexity | Grouping the data is O(n), where n = nb of rows. Then insertion sort is O(d²) for each participant, where d = nb of days for one participant. So overall, the baseline is around O(n + p × d²), where p = nb of participants. |
| Expected space complexity | O(n), because I store the days grouped by participant before sorting them. |
| How I tested | I tested with a small fake dataset first, so I could check the result by hand. I checked that each participant had the right days, that the result had maximum 5 days, and that the days were sorted from highest steps to lowest steps. |
| Python file | src/A2_Intermediate.py AND src/A2_Test.py |

### Result
This analysis gives the 5 days with the highest number of steps for each participant. For the baseline, I used insertion sort. I sort all the days of a participant by step count in descending order, then I take the first five days. This works and it is close to the course, but it is not the most efficient because I sort the whole list even though I only need five days.

### Note about debugging :)
At first, the code did not work correctly because I was reading the wrong columns from the CSV file. I had to check the structure of the dataset again and remember that index 0 is the date, and index 1 is the number of steps. After fixing the column indexes, the grouping and sorting logic worked as expected. This helped me understand that even if the algorithm is correct, the result can still be wrong if the input data is not read properly.

