from datetime import datetime, timedelta

class Match:
    def __init__(self, home_team, away_team, location, start_time):
        self.home_team = home_team
        self.away_team = away_team
        self.location = location
        self.start_time = start_time
        self.home_goals = 0
        self.away_goals = 0
        self.played = False

    def play(self):
        # Implementation of match simulation
        self.result = simulate_match(self.home_team, self.away_team)




