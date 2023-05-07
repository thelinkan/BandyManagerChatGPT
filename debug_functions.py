

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

