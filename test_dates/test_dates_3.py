from datetime import datetime, timedelta

def get_evenly_spaced_dates(dates_list, num_dates):
    # Convert dates_list to datetime objects
    datetime_list = [datetime(*date) for date in dates_list]
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
        current_date += timedelta(days=days_per_date)
    return evenly_spaced_dates


dates_list = [(2023, 11, 10), (2023, 11, 17), (2023, 11, 24), (2023, 12, 1), (2023, 12, 8), (2023, 12, 15), (2023, 12, 22), (2023, 12, 29), (2024, 1, 5), (2024, 1, 12), (2024, 1, 19), (2024, 1, 26), (2024, 2, 2), (2024, 2, 9)]

evenly_spaced_dates = get_evenly_spaced_dates(dates_list, 5)
print(evenly_spaced_dates)

evenly_spaced_dates = get_evenly_spaced_dates(dates_list, 7)
print(evenly_spaced_dates)
