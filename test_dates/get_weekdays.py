import datetime

def get_weekdays(start_date, end_date, weekday):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_idx = weekdays.index(weekday)

    start_date = datetime.date(*start_date)
    end_date = datetime.date(*end_date)

    days = (end_date - start_date).days + 1
    weekdays_list = [start_date + datetime.timedelta(days=x) for x in range(days) if (start_date + datetime.timedelta(days=x)).weekday() == weekday_idx]

    return [(d.year, d.month, d.day) for d in weekdays_list]

