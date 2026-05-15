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
| Python file | src/A1_Beginner.py AND src/A1_Test.py |

### Result

The participant with the highest 10k step goal achievement rate is participant 7359, with a success rate of 94.83%.


# Analysis 2: Top 5 active days per participant

## Problem
- Find the top 5 most active days for each participant
- Based on daily step count
- Continuation of Analysis 1:
  - Analysis 1 = regularity with 10k goal
  - Analysis 2 = strongest activity days

## Algorithm
- Compare two approaches:  baseline + improved version

### Baseline

- Group days by participant
- For each participant:
  - take all recorded days
  - sort all days by step count
  - descending order
  - keep first 5 days
- Sorting algorithm used: insertion sort
- Simple and close to the course
- Not optimal because it sorts the whole list where as only 5 days are act. needed

### Improved version

- Not yet

## Why this algorithm?

- Baseline:
  - easy to understand
  - based on insertion sort from the course
  - good comparison point
- Goal:
  - compare simple correct solution vs more efficient solution

## Complexity

- Baseline:
  - insertion sort
  - worst-case time complexity: O(n^2) per participant
  - because each day may be compared with many previous days
- Improved version:
  - Will do tomorrow :) 

## Tests

- Idk yet

Python files: src/A2_Intermediate.py and probably src/A2_Test.py
