# Analysis 2: Top 5 active days per participant


#df y3ne = receive the CSV
def group_days_by_participant(df):
    #This empty dictionary (then store something) where key=idparticip and value=list de jours+ses pas
    days_by_participant = {}

    #We go through the dataset row by row 
    for index, row in df.iterrows():
        participant = row["participant_id"]
        date = row["DATE"]
        steps = row["ACTIVITY_steps"]

        #if first time see this participant then create an empty list
        if participant not in days_by_participant:
            days_by_participant[participant] = []

        #add this day to the participant's list
        days_by_participant[participant].append((date, steps)) #("06.07.21, 12000")-> tuple btw

    return days_by_participant


def insertion_sort_days_by_steps(days):
    #A copy bcs we dont wanna change the original list
    sorted_days = days.copy()

    #Start at index 1 because the 1st elem. alone is already sorted
    for current_index in range(1, len(sorted_days)):
        day_to_insert = sorted_days[current_index]
        scan_index = current_index - 1 #compare with the left number

        #We shift smaller step counts to the right
        #We want descending order, so bigger step counts come first 
        while scan_index >= 0 and sorted_days[scan_index][1] < day_to_insert[1]:
            sorted_days[scan_index + 1] = sorted_days[scan_index]
            scan_index = scan_index - 1

        # We insert the day at the correct position.
        sorted_days[scan_index + 1] = day_to_insert

    return sorted_days


def top_k_days_baseline(df, k=5):
    #Awalan, group the days by participant
    days_by_participant = group_days_by_participant(df)

    # Dictionary will store the top k days for each participant
    top_days = {}

    #Go through every participant 1 by 1
    for participant in days_by_participant:
        days = days_by_participant[participant]

        # Baseline: sort all days, even if we only need the first k.
        sorted_days = insertion_sort_days_by_steps(days)

        # Keep only the first k days.
        top_days[participant] = sorted_days[:k]

    return top_days