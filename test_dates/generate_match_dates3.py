def generate_match_dates(date_list1, date_list2, date_list3, num_rounds):
    match_dates = []
    dates = [date_list1, date_list2, date_list3]
    round_dates = [[] for _ in range(num_rounds)]

    # Use the first date from the first list and remove it
    round_dates[0].append(dates[0].pop(0))

    # Calculate the number of rounds that can be filled with 2 dates per round
    num_two_dates = min(num_rounds-1, len(dates[1]), len(dates[2]))
    for i in range(num_two_dates):
        # Prioritize using the first and last dates from the list
        if len(dates[1]) >= 2 and i % 2 == 0:
            round_dates[i+1].extend([dates[1].pop(0), dates[1].pop()])
        elif len(dates[2]) >= 2 and i % 2 == 1:
            round_dates[i+1].extend([dates[2].pop(0), dates[2].pop()])
        else:
            # If the first and last dates are already used, use the closest dates to the middle instead
            index1 = len(dates[1]) // 2
            index2 = len(dates[2]) // 2
            if i % 2 == 0 and len(dates[1]) > 0:
                round_dates[i+1].append(dates[1].pop(index1))
            elif i % 2 == 1 and len(dates[2]) > 0:
                round_dates[i+1].append(dates[2].pop(index2))

    # Fill remaining rounds with one date per round
    for i in range(num_two_dates+1, num_rounds):
        for j in range(3):
            if len(dates[j]) > 0:
                round_dates[i].append(dates[j].pop(0))
                break

    # Flatten the list of round dates and sort them
    match_dates = [date for round in round_dates for date in round]
    match_dates.sort()

    return match_dates
