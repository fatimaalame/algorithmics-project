# Analysis 1: 10,000 steps goal %

# fonction 1 = calcule les pourcentages
# fonction 2 = cherche le meilleur pourcentage

# pandas = to manipulate tableau CSV
import pandas as pd 


def calculate_10k_goal_rate(df):
    # Two empty dictionary to count days for each participant
    total_days = {}   #count days
    goal_days = {}    #count days with >= 10000 pas 

    #Go through the dataset row by row
    for index, row in df.iterrows():
        participant = row["participant_id"]  #récupère id + ses pas 
        steps = row["ACTIVITY_steps"]

        #First time we see this participant then create counters from 0
        if participant not in total_days:
            total_days[participant] = 0
            goal_days[participant] = 0

        # Every row counts as one recorded day
        total_days[participant] = total_days[participant] + 1

        # Goal day = at least 10,000 steps
        if steps >= 10000:
            goal_days[participant] = goal_days[participant] + 1

    #Now, on calcule the percentage for each participant
    rates = {}

    for participant in total_days:
        rate = goal_days[participant] / total_days[participant] * 100
        rates[participant] = rate

    return rates

# I first compute the success rate for each participant using dictionaries.
# Then I scan these rates to find the participant with the highest rate.
# This is a linear search for the maximum.

def find_best_participant(rates):
    #At the start, we dont know who is the best participant
    best_participant = None
    best_rate = -1

    #We look at each participant and their rate, in the dictionary 
    for participant in rates:
        if rates[participant] > best_rate:
            best_rate = rates[participant] #Then on remplace
            best_participant = participant

    return best_participant, best_rate   #We renvoie le participant + his %

