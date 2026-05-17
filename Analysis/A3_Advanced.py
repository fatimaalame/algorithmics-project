#Analysis 3: Longest 10k steps streak

from datetime import datetime

def convert_date(date_text):
    #Convert the date from text -> real Python date
    #Example in the dataset: "06.07.21"
    return datetime.strptime(str(date_text), "%d.%m.%y").date()

