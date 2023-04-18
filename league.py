import random
from team import Team
from match import Match
from country import Country
from miscfunctions import return_schedule

class League:
    def __init__(self, name, country, level,teams , num_rounds, win_points=2, draw_points=1, start_year = 2023, start_month=11, start_day=1, end_month=2, end_day=15, match_manager=None):
        self.name = name
        self.country = country
        self.num_teams = len(teams)
        self.num_rounds = num_rounds
        self.win_points = win_points
        self.draw_points = draw_points
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.end_month = end_month
        self.end_day = end_day
        self.teams = teams
        self.matches = []
        self.table = {team: {'played': 0, 'won': 0, 'drawn': 0, 'lost': 0, 'goals_for': 0, 'goals_against': 0, 'points': 0} for team in teams}
        self.match_manager = match_manager

    def generate_schedule(self):
        schedule = return_schedule(self.num_teams,self.num_rounds)
        r_year = self.start_year
        r_month = self.start_month
        r_day = self.start_day
        for round in schedule:
            for match in round:
                match = Match(self.teams[match[0]],self.teams[match[1]],r_year,r_month,r_day)
                self.matches.append(match)
                if self.match_manager is not None:
                    self.match_manager.add_match(match,self)
            r_day += 7
            if(r_day>30):
                r_day = r_day - 30
                r_month += 1
                if(r_month>12):
                    r_month = r_month - 12
                    r_year += 1
                #print(f"{match[0]}  -  {match[1]}")
                #print(f"{self.teams[match[0]].name}  -  {self.teams[match[1]].name}")


    def get_all_matches(self):
        return self.matches

    def get_matches_by_date(self, date):
        return [match for match in self.matches if match.start_time.date() == date]

    def get_matches_by_team(self, team):
        return [match for match in self.matches if team in [match.home_team, match.away_team]]

    def to_dict(self):
        return {
            'name': self.name,
            'country': self.country,
            'num_teams': self.num_teams,
            'num_rounds': self.num_rounds,
            'win_points': self.win_points,
            'draw_points': self.draw_points,
            'start_year': self.start_year,
            'start_month': self.start_month,
            'start_day': self.start_day,
            'end_month': self.end_month,
            'end_day': self.end_day,
            'teams': [team.name for team in self.teams],
            'matches': [match.to_dict() for match in self.matches],
        }

    def calculate_table(self):
        for team in self.table:
            self.table[team] = {'played': 0, 'won': 0, 'drawn': 0, 'lost': 0, 'goals_for': 0, 'goals_against': 0, 'points': 0}

        for match in self.matches:
            if match.played:
                home_team = match.home_team
                away_team = match.away_team
                home_goals = match.home_goals
                away_goals = match.away_goals

                self.table[home_team]['played'] += 1
                self.table[away_team]['played'] += 1

                if home_goals > away_goals:
                    self.table[home_team]['won'] += 1
                    self.table[home_team]['points'] += self.win_points
                    self.table[away_team]['lost'] += 1
                elif home_goals < away_goals:
                    self.table[away_team]['won'] += 1
                    self.table[away_team]['points'] += self.win_points
                    self.table[home_team]['lost'] += 1
                else:
                    self.table[home_team]['drawn'] += 1
                    self.table[home_team]['points'] += self.draw_points
                    self.table[away_team]['drawn'] += 1
                    self.table[away_team]['points'] += self.draw_points

                self.table[home_team]['goals_for'] += home_goals
                self.table[home_team]['goals_against'] += away_goals
                self.table[away_team]['goals_for'] += away_goals
                self.table[away_team]['goals_against'] += home_goals

    def print_table(self):
        print("{:<20} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6}".format("Team", "Pld", "W", "D", "L", "GF", "GA", "Pts"))
        sorted_table = sorted(self.table.items(), key=lambda x: (x[1]['points'], x[1]['goals_for'] - x[1]['goals_against']), reverse=True)
        for team, stats in sorted_table:
            print("{:<20} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6}".format(team.name, stats['played'], stats['won'], stats['drawn'], stats['lost'], stats['goals_for'], stats['goals_against'], stats['points']))

    def print_schedule(self):
        for i, round in enumerate(self.rounds):
            print(f"Round {i + 1}:")
            for game in round:
                print(f"{game.home_team} vs. {game.away_team}")