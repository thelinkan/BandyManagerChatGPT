import datetime
#from datetime import datetime, timedelta

def get_weekdays(start_date, end_date, weekday):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_idx = weekdays.index(weekday)

    start_date = datetime.date(*start_date)
    end_date = datetime.date(*end_date)

    days = (end_date - start_date).days + 1
    weekdays_list = [start_date + datetime.timedelta(days=x) for x in range(days) if (start_date + datetime.timedelta(days=x)).weekday() == weekday_idx]

    return [(d.year, d.month, d.day) for d in weekdays_list]

def get_evenly_spaced_dates(dates_list, num_dates):
    # Convert dates_list to datetime objects
    datetime_list = [datetime.datetime(*date) for date in dates_list]
    # Calculate time interval between first and last date
    time_interval = datetime_list[-1] - datetime_list[0]
    # Calculate the number of days between the first and last date
    num_days = time_interval.days
    # Calculate the number of days between each date
    days_per_date = num_days / (num_dates - 1)
    # Create a list of evenly spaced dates
    evenly_spaced_dates = []
    current_date = datetime_list[0]
    for i in range(num_dates):
        evenly_spaced_dates.append((current_date.year, current_date.month, current_date.day))
        current_date += datetime.timedelta(days=days_per_date)
    return evenly_spaced_dates
    
def sort_by_date(dates):
    return datetime.date(*dates)    