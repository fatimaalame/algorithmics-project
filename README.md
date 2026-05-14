# Applied Algorithms Project

## Student: 
Fatima Alame (22-836-563)

## Project context
This project is part of the Applied Algorithms course at the University of Geneva.

The goal of the project is to work with a real dataset and apply algorithmic concepts in Python. The project focuses on reading, processing, analysing, and interpreting data using algorithms and data structures studied during the course.

## Current structure

```text
projet_AA/
├── data/
│   └── merged.csv              #from the exos and used for my analyses
├── notebooks/
├── researchdata/               #raw dataset, that gotta be ignored by Git
│   ├── 1487.csv
│   ├── 1488.csv
│   └── ...                     #our 12 participant files
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── prepare_data.py
    ├── A1_Beginner.py
    └── A1_Test.py
├── venv/                       #local virtual environment, ignored by Git
├── .gitignore
├── README.md
└── requirements.txt
```

## Analysis 1 — 10,000 Steps Goal Achievement Rate

| Field | My answer |
|---|---|
| Problem I want to solve | Which participant reaches the 10,000-step goal most consistently? |
| Algorithm I will use | I use a linear scan through all rows of the dataset. For each participant, I count the total number of recorded days and the number of days where they reached at least 10,000 steps. Then I calculate the success rate for each participant and scan the results to find the highest rate. |
| Why this algorithm is appropriate | This is a simple counting problem. Each row only needs to be checked once, so a linear scan is enough. Dictionaries are useful because each participant can be stored as a key, with their counters as values. I chose a percentage instead of only counting days because participants may not all have the same number of recorded days. |
| Expected time complexity | O(n + p), usually simplified to O(n), where n = nb of rows and p = nb of participants. |
| Expected space complexity | O(p), because the algorithm stores counters and rates for each participant. |
| Minimum tests | I tested the function on a small fake dataset where the expected result can be calculated by hand but I also tested it on the real merged dataset and checked that the final percentage is between 0 and 100. |
| Python file | `src/A1_Beginner.py` AND `src/A1_Test.py` |

### Result

On the real merged dataset, the participant with the highest 10,000-step goal achievement rate is participant `7359`, with a success rate of approximately `94.83%`.