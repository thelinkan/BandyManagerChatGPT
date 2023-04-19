from get_weekdays import get_weekdays
from generate_match_dates3 import generate_match_dates



wednesdays = get_weekdays((2023, 4, 10), (2023, 4, 30), "Wednesday")
fridays = get_weekdays((2023, 4, 10), (2023, 4, 30), "Friday")
sundays = get_weekdays((2023, 4, 10), (2023, 4, 30), "Sunday")
print(wednesdays) # Output: [(2023, 4, 12), (2023, 4, 19), (2023, 4, 26)]
print(fridays) # Output: [(2023, 4, 12), (2023, 4, 19), (2023, 4, 26)]
print(sundays) # Output: [(2023, 4, 12), (2023, 4, 19), (2023, 4, 26)]
round_days = generate_match_dates(sundays, fridays,wednesdays,6)

print(wednesdays) # Output: [(2023, 4, 12), (2023, 4, 19), (2023, 4, 26)]
print(fridays) # Output: [(2023, 4, 12), (2023, 4, 19), (2023, 4, 26)]
print(sundays) # Output: [(2023, 4, 12), (2023, 4, 19), (2023, 4, 26)]
print(round_days)

#weekdays = get_weekdays((2023, 10, 20), (2024, 2, 20), "Sunday")
#print(weekdays) # Output: [(2023, 4, 12), (2023, 4, 19), (2023, 4, 26)]

#num_days = len(weekdays)

#print(f"Number of Sundays: {num_days}")
