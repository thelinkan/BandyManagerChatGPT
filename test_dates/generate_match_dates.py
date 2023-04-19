def generate_match_dates(dates1, dates2, dates3, num_rounds):
    all_dates = dates1 + dates2 + dates3
    round_dates = []
    i = 0
    while i < num_rounds:
        if i < len(dates1):
            round_dates.append(dates1[i])
            i += 1
        else:
            available_dates = all_dates[i:]
            if len(available_dates) >= 3:
                round_dates.append(available_dates[0])
                round_dates.append(available_dates[1])
                round_dates.append(available_dates[2])
                i += 3
            else:
                round_dates += available_dates
                i += len(available_dates)
    return round_dates
