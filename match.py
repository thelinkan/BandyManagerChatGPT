from datetime import datetime, timedelta
import random

class Match:
    def __init__(self, home_team, away_team, year, month, day):
        self.home_team = home_team
        self.away_team = away_team
        self.year = year
        self.month = month
        self.day = day
        self.home_goals = 0
        self.away_goals = 0
        self.played = False

    def play(self):
        self.home_goals = random.randint(0, 10)
        self.away_goals = random.randint(0, 10)
        self.played = True

    def load_match(self, home_goals, away_goals,played):
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.played = played
        #print (f"{self.home_team.name} - {self.away_team.name}    {self.home_goals}-{self.away_goals}")
        
    def to_dict(self):
        print (f"{self.home_team.name} - {self.away_team.name}    {self.home_goals}-{self.away_goals}")
        return {
            'home_team': self.home_team.name,
            'away_team': self.away_team.name,
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'home_goals': self.home_goals,
            'away_goals': self.away_goals,
            'played': self.played
        }


