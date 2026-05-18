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

| Algorithm I will use | I compare two approaches. The baseline groups the days by participant, sorts all days with insertion sort, and keeps the first 5 days. The improved approach uses a top-k selection strategy: it scans the days once and only keeps a small sorted list of the best k days. |

| Why this algorithm is appropriate | It's because I compare a baseline approach with an improved approach. The baseline is simple and close to the course, but it sorts all days. The improved version is better because I only need the top 5 days, so I keep only a small top-k list instead of sorting everything. |

| Expected time complexity | Grouping the data is O(n), where n = number of rows. For the baseline, insertion sort is O(d²) for each participant, where d = number of days for one participant. For the improved version, the complexity is O(d × k) for each participant, because I scan the days and maintain a small list of size k. Since k = 5, this is close to O(d). |

| Expected space complexity | The grouping step uses O(n), because I store the days grouped by participant. The baseline also stores a sorted copy of the days. The improved version only keeps a small top-k list for each participant while scanning. |

| How I tested | I tested with a small fake dataset first, so I could check the result by hand. I compared the baseline version, the improved version, and Python's built-in sorted version. I also tested the real dataset, an edge case where a participant has fewer days than k, and I included an intentionally failing test in the code but left it commented out. |

| Python file | Analysis/A2_Intermediate.py |

### Results
The different tests dataset confirm that the algorithm works as expected :)  (they all got the same results)

### Interpretation
The fake dataset confirms that the algorithm works correctly, because the baseline, improved, and built-in sorted versions all return the same top days.

For the real dataset, participant 7359 has the highest activity on 01.11.21 with 27416 steps. The top 5 days are all above 22000 steps, which shows several strong activity peaks.

The improved version gives the same result as the baseline, but avoids sorting all days. This makes sense because I only need the top 5 days, not the full sorted list.

### Note about debugging :)
At first, the code did not work correctly because I was reading the wrong columns from the CSV file. I had to check the structure of the dataset again and remember that index 0 is the date, and index 1 is the number of steps. After fixing the column indexes, the grouping and sorting logic worked as expected. This helped me understand that even if the algorithm is correct, the result can still be wrong if the input data is not read properly. 

