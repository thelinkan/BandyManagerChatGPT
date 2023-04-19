def generate_match_dates(date_list1, date_list2, date_list3, rounds):
    match_dates = []

    # add dates from first list until we have enough rounds
    for date in date_list1:
        if len(match_dates) >= rounds:
            break
        match_dates.append(date)

    # calculate the number of remaining rounds to fill
    remaining_rounds = rounds - len(match_dates)

    # calculate the number of dates needed from each of the other two lists
    num_dates_from_list2 = (remaining_rounds + 1) // 2
    num_dates_from_list3 = remaining_rounds - num_dates_from_list2

    # add dates from second list
    for i in range(num_dates_from_list2):
        if i < len(date_list2):
            match_dates.append(date_list2[i])

    # add dates from third list
    for i in range(num_dates_from_list3):
        if i < len(date_list3):
            match_dates.append(date_list3[i])

    # sort the list by date
    match_dates.sort(key=lambda date: date[0])

    return match_dates
