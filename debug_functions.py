from miscfunctions import yesterday


def print_playoff_series(series):
    print("Print Playoff Series")
    print("====================")
    #print(series)
    home_team = series["home_team"]
    home_team_wins = series["home_team_wins"]
    away_team = series["away_team"]
    away_team_wins = series["away_team_wins"]
    winner_team = series["winner_team"]
    matches = series["matches"]
    print(f"Teams: {home_team.name} - {away_team.name}")
    print(f"Won games: {home_team_wins} - {away_team_wins}")
    if winner_team is not None:
        print(f"Team {winner_team.name} won the series")
    print("Matches:")
    #print(matches)
    i = 0
    for match in matches:
        i += 1
        print(f"    --   date     : {match.year} {match.month} {match.day}")
        print(f"    --   match {i}: {match.home_team.name} - {match.away_team.name}    {match.home_goals} - {match.away_goals}")
    print("====================")
    print("")

def print_yesterdays_results(game):
    year_yesterday, month_yesterday, day_yesterday = yesterday(game.year, game.month, game.day)
    matches_today = game.match_manager.get_matches_by_date(year_yesterday, month_yesterday, day_yesterday)

    print("========================================")
    print("|                                      |")
    print("|    DEBUG: Yesterdays results         |")
    print("|                                      |")
    print(f"|  {game.year}-{game.month}-{game.day}              |")   
    print("|                                      |")
    print("========================================")    

    if len(matches_today) > 0:
        for match in matches_today:
            match_league = game.match_manager.get_league_of_match(match)
            print (f"{match_league.name}: {match.home_team.name} - {match.away_team.name}")



    print("========================================")
    print("|                                      |")
    print("|              END DEBUG               |")
    print("|                                      |")
    print("========================================")    

def debugprint_playoff(playoff):
    print("========================================")
    print("|                                      |")
    print("|    DEBUG: playoff                    |")
    print("|                                      |")
    print("========================================")    
    print(playoff.name)
    print("========================================")

    print("Teams")
    for team in playoff.teams:
        print(team.name)
    print()
    print(f"  is started: {playoff.is_started}")

    #print(playoff.rounds)
    for round in playoff.rounds:
        if (round == "Quarterfinals"):
            serieses = ["Quarterfinal 1","Quarterfinal 2","Quarterfinal 3","Quarterfinal 4"]
        if (round == "Semifinals"):
            serieses = ["Semifinal 1","Semifinal 2"]
        if (round == "Finals"):
            serieses = ["Final 1"]
        round_data = playoff.rounds[round]
        is_scheduled = round_data["is_scheduled"]
        is_completed = round_data["is_completed"]
        print(round)
        print(f"  is scheduled: {is_scheduled}")
        print(f"  is completed: {is_completed}")
        print("")
        if is_scheduled:
            for series in serieses:
                series_data = round_data[series]
                home_team = series_data["home_team"]
                away_team = series_data["away_team"]
                home_team_wins = series_data["home_team_wins"]
                away_team_wins = series_data["away_team_wins"]
                winner_team = series_data["winner_team"]
                matches = series_data["matches"]
                print("")
                print(f"    {series}")    
                print(f"    {home_team.name} - {away_team.name}: {home_team_wins} - {away_team_wins}")    
                if winner_team is not None:
                    print(f"      Winner - {winner_team.name}")
                for match in matches:
                    #match_home_team = match.home_team
                    #match_home_team = match.awa
                    print(f"        {match.home_team.name} - {match.away_team.name}: {match.home_goals} - {match.away_goals}")
                #print(series_data)

        #print(round_data)

    print("========================================")
    print("|                                      |")
    print("|              END DEBUG               |")
    print("|                                      |")
    print("========================================")


