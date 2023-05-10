import datetime
#from datetime import datetime, timedelta
from miscfunctions import get_k_integers

def get_weekdays(start_date, end_date, weekday):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_idx = weekdays.index(weekday)

    start_date = datetime.date(*start_date)
    end_date = datetime.date(*end_date)

    days = (end_date - start_date).days + 1
    weekdays_list = [start_date + datetime.timedelta(days=x) for x in range(days) if (start_date + datetime.timedelta(days=x)).weekday() == weekday_idx]

    return [(d.year, d.month, d.day) for d in weekdays_list]

def get_evenly_spaced_dates(dates_list, num_dates):
    num_dates_total = len(dates_list)
    if num_dates >= num_dates_total:
        return dates_list
    integer_list = get_k_integers(num_dates_total,num_dates)
    result = set()
    for i in integer_list:
        result.add(dates_list[i])
    return list(result)
    
def sort_by_date(dates):
    return datetime.date(*dates)    