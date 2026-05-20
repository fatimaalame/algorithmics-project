# AA Project

## Student: 
Fatima Alame (22-836-563)

## Project context

I'm working with real smartwatch data (provided by the uni) and using Python to explore daily activity patterns. The goal is not only to read the dataset, but also to apply the algorithmic ideas we got in class in a concrete way. I focus on writing simple functions, using loops and dictionaries, testing my code, and explaining why each algorithm made sense to me.


## Data instructions

Before running the project, the dataset must be placed in this folder:

```text
data/
```

The expected file path is:

```text
data/merged.csv
```
-> The original private dataset is not included in the GitLab repository. It has to stay local on the computer. In my project, the scripts expect a local file called data/merged.csv

The scripts expect the dataset to contain at least these columns:

```text
DATE
DAY_OF_THE_WEEK
ACTIVITY_steps
```

The dataset also needs a participant identifier column, used to group the data by participant.

If `merged.csv` is missing or placed in another folder, the scripts will not be able to load the data correctly.

## Installation

This project uses Python. A virtual environment can be used to keep the project dependencies separate from the rest of the computer.

On macOS, the virtual environment can be created/activated with:

```bash
python -m venv venv
source venv/bin/activate
```

Then the required packages can be installed with:

```bash
pip install -r requirements.txt
```

## How to run the project

The code should be executed from the root folder of the repository.

Example:

```bash
cd projet_AA
```

Then each analysis can be run separately.

To run Analysis 1:

```bash
python Analysis/A1_Beginner.py
```

To run Analysis 2:

```bash
python Analysis/A2_Intermediate.py
```

To run Analysis 3:

```bash
python Analysis/A3_Advanced.py
```

Each script prints its result directly in the terminal (because I included the tests right in the files themselves)

## How to read the results

The three analyses answer different questions.

Analysis 1 answers:

```text
Who reaches the 10,000-step goal most often?
```

Analysis 2 answers:

```text
What are the highest-activity days for each participant?
```

Analysis 3 answers:

```text
Who keeps an active routine over consecutive days?
```

## Tests
I included simple assert tests directly in the analysis files. They check normal cases and some edge cases.

I also added intentionally failing tests, as requested in the  instructions but I left them commented out so the files can still run normally. If you'd like to see them fail, you can  remove the # before the failing assert and run the file again.


# Analysis 1: 10k steps goal achievement %

| Field | My answer |
|---|---|
| Problem I want to solve | Which participant reaches the 10k step goal most consistently? |
| Algorithm I will use | I use a linear scan through all the rows of the dataset. For each participant, I count the total number of recorded days and the number of days where they reached at least 10k steps. Then I calculate the success rate for each participant and scan the results to find the highest rate. |
| Why this algorithm is appropriate | This is a simple counting problem. Each row only needs to be checked once, so a linear scan is enough. Dictionaries are useful because each participant can be stored as a key, with their counters as values. I chose a percentage instead of only counting days because participants may not all have the same number of recorded days (so that'd be cheating for some participants). |
| Expected time complexity | O(n + p), usually simplified to O(n), where n = nb of rows and p = nb of participants. |
| Expected space complexity | O(p), because the algorithm stores counters and rates for each participant. |
| How I tested | I tested the function on a small fake dataset where the expected result can be calculated by hand but I also tested it on the real merged dataset and checked that the final percentage is between 0 and 100. |
| Python file | [Analysis/A1_Beginner.py](Analysis/A1_Beginner.py) |

### Results

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
| Python file | [Analysis/A2_Intermediate.py](Analysis/A2_Intermediate.py) |

### Results
All three versions (baseline, improved, built-in) return identical results on both the fake and real datasets.

### Interpretation
The fake dataset confirms that the algorithm works correctly, because the baseline, improved, and built-in sorted versions all return the same top days. For the real dataset, participant 7359 has the highest activity on 01.11.21 with 27416 steps. The top 5 days are all above 22000 steps, which shows several strong activity peaks. The improved version gives the same result as the baseline, but avoids sorting all days. This makes sense because I only need the top 5 days, not the full sorted list.

### Note about debugging :)
At first, the code did not work correctly because I was reading the wrong columns from the CSV file. I had to check the structure of the dataset again and remember that index 0 is the date, and index 1 is the number of steps. After fixing the column indexes, the grouping and sorting logic worked as expected. This helped me understand that even if the algorithm is correct, the result can still be wrong if the input data is not read properly. 



# Bonus Analysis 3: Longest streak 10k steps

This analysis is optional but I did it because it studies consistency over consecutive days.

| Field | My answer |
|---|---|
| Problem I want to solve | Which participant has the longest consecutive streak of days with at least 10k steps? |
| Algorithm I will use | First, I group the days by participant with a dictionary. Then, for each participant, I sort the days by date so I can read them in chronological order. After that, I scan the days one by one and keep two values: the current streak and the longest streak found so far. |
| Why this algorithm is appropriate | This problem is about consistency over time, not just one isolated high value. I need to check if active days follow each other without a gap. The scan is appropriate because each participant's days can be checked in order, and the streak can be updated step by step. This is close to a dynamic-programming idea (took the idea from course 4, exo 5), because the current streak is computed from the previous streak. However, in the implementation, it stays simple: I only keep the current streak and the best streak found so far. |
| Expected time complexity | For each participant, sorting the days by date costs O(d log d), where d = number of days for one participant. Then scanning the sorted days costs O(d). So the total is dominated by the sorting step. |
| Expected space complexity | The grouping step uses O(n), because I store the days grouped by participant. During the streak scan, I only keep a few variables like current_streak and longest_streak, so the extra space for the scan is O(1). |
| How I tested | I tested with a fake dataset where I could calculate the streaks by hand. I also added edge cases: a participant with no active days, and a missing calendar day that should break the streak. Finally, I tested the algorithm on the real merged dataset. |
| Python file | [Analysis/A3_Advanced.py](Analysis/A3_Advanced.py) |

### Results
The fake dataset tests passed. Participant A has a longest streak of 3 days, and participant B has a longest streak of 2 days. On the real dataset, the participant with the longest 10k-step streak is participant 7359, with a streak of 36 consecutive active days.

### Interpretation
This result shows that participant 7359 is not only active on isolated days, but also has the strongest regularity over time. A streak of 36 days means that this participant reached at least 10k steps every day for more than one month.

# In conclusion
This analysis (A3) is different from A1 and A2 because it focuses on consecutive behavior. A1 measures the general success rate, A2 finds the highest activity peaks, and A3 checks long-term consistency.

# Notice on the use of AI tools
I used AI tools during this project to help me understand the course material, debug some (a lot actually) Python errors, add more structured comments but also check if my algorithms matched the expected project level (very important).
AI was also very useful for reformulating my documentation, especially the README. It helped make my explanations clearer and way more structured while keeping the content based on me trying to explain all I did. I used: GPT thinking 5.5 + Claude Sonnet 4.6