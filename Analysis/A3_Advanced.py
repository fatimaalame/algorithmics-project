#Analysis 3: longest streak 10k steps

from datetime import datetime

def convert_date(date_text):
    #Dates in the CSV are written like "06.07.21"
    #I convert them so Python can sort them properly later
    return datetime.strptime(str(date_text), "%d.%m.%y").date()


def group_days_by_participant(data):
    #I put all days of the same participant together

    participants = {}

    for row in data:
        participant_id = row["participant_id"]
        date = convert_date(row["DATE"])
        steps_float = float(row["ACTIVITY_steps"])

        #Some rows got no step value, so I skip them
        if steps_float != steps_float:
            continue

        steps = int(steps_float)

        if participant_id not in participants:
            participants[participant_id] = []

        participants[participant_id].append((date, steps))

    return participants
