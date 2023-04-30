dates = [(2023, 11, 10), (2023, 11, 17), (2023, 11, 24), (2023, 12, 1), (2023, 12, 8), (2023, 12, 15), (2023, 12, 22), (2023, 12, 29), (2024, 1, 5), (2024, 1, 12), (2024, 1, 19), (2024, 1, 26), (2024, 2, 2), (2024, 2, 9)]
n = 11
step = len(dates) // n
selected_dates = [dates[i] for i in range(0, len(dates), step)]
print(f"{dates} --- {len(dates)}")
print(selected_dates)
