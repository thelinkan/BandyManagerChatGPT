import random
from team import Team
from matchcode.match import Match
from country import Country
from miscfunctions import return_schedule, adddays
from datecode.date_functions import get_weekdays, get_evenly_spaced_dates, sort_by_date

class League:
    def __init__(self, name, country, team_type, level, league_type ,teams , num_rounds, win_points=2, draw_points=1, start_year = 2023, start_month=11, start_day=1, end_month=2, end_day=15, match_manager=None):
        self.name = name
        self.country = country
        self.team_type = team_type
        self.level = level
        self.league_type = league_type
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
        self.playoff_for_league = None
        self.is_playoff = False
        self.is_started = False
        self.qualification_league_up = None
        self.qualification_league_down = None
        self.num_teams_moved_up = 0
        self.moved_up_to_level = 0
        self.num_teams_to_qualification_up = 0
        self.num_teams_to_qualification_down = 0
        self.num_teams_moved_down = 0
        self.moved_down_to_level = 0


        self.num_teams_to_playoff = 0

        if self.start_month > self.end_month:
            self.end_year = self.start_year + 1
        else:
            self.end_year = self.start_year

        if self.league_type == "Normal":
            self.is_started = True

    def generate_schedule(self):
        schedule = return_schedule(self.num_teams,self.num_rounds)

        sundays = get_weekdays((self.start_year, self.start_month, self.start_day), (self.end_year, self.end_month, self.end_day),"Sunday")
        fridays = get_weekdays((self.start_year, self.start_month, self.start_day), (self.end_year, self.end_month, self.end_day),"Friday")
        wednesdays = get_weekdays((self.start_year, self.start_month, self.start_day), (self.end_year, self.end_month, self.end_day),"Wednesday")
        print(f"{self.start_year} - {self.start_month} - {self.start_day}")
        print(f"Sundays {sundays}")
        if self.num_rounds > len(sundays):
            rounds_left = self.num_rounds - len(sundays)
            fridays_to_play = get_evenly_spaced_dates(fridays, rounds_left)
            #print(f"Fridays {fridays_to_play}")
            sorted_dates = sorted(sundays + fridays_to_play, key=lambda date: sort_by_date(date))
        if self.num_rounds == len(sundays):
            sorted_dates = sorted(sundays, key=lambda date: sort_by_date(date))
        #print(f"sundays {len(sundays)}")
        #print(sorted_dates)
        i = 0
        for round in schedule:
            print(f"round {i}")
            round_date = sorted_dates[i]
            r_year = round_date[0]
            r_month = round_date[1]
            r_day = round_date[2]
            for match in round:
                match = Match(self.teams[match[0]],self.teams[match[1]],r_year,r_month,r_day)
                self.matches.append(match)
                if self.match_manager is not None:
                    self.match_manager.add_match(match,self)
                print(match)
            #r_year, r_month, r_day = adddays(r_year, r_month, r_day, 7)
            i += 1

    def load_schedule(self,matches,teams):
        #print(teams['Sandvikens AIK'])
        for match in matches:
            home_team = teams[match['home_team']]
            away_team = teams[match['away_team']]
            year = match['year']
            month = match['month']
            day = match['day']
            home_goals = match['home_goals']
            away_goals = match['away_goals']
            played = match['played']
            new_match = Match(home_team,away_team,year,month,day)
            new_match.load_match(home_goals,away_goals,played)
            self.matches.append(new_match)
            if self.match_manager is not None:
                self.match_manager.add_match(new_match,self)
                #print(new_match)
            #print(match)

    def promotion_relegation(self,promotion_relegation):
        if ("qualification_league_up" in promotion_relegation):
            self.qualification_league_up = promotion_relegation["qualification_league_up"]
        if ("qualification_league_down" in promotion_relegation):
            self.qualification_league_down = promotion_relegation["qualification_league_down"]
        if ("num_teams_moved_up" in promotion_relegation):
            self.num_teams_moved_up = promotion_relegation["num_teams_moved_up"]
        if ("moved_up_to_level" in promotion_relegation):
            self.moved_up_to_level = promotion_relegation["moved_up_to_level"]
        if ("num_teams_to_qualification_up" in promotion_relegation):
            self.num_teams_to_qualification_up = promotion_relegation["num_teams_to_qualification_up"]
        if ("num_teams_to_qualification_down" in promotion_relegation):
            self.num_teams_to_qualification_down = promotion_relegation["num_teams_to_qualification_down"]
        if ("num_teams_moved_down" in promotion_relegation):
            self.num_teams_moved_down = promotion_relegation["num_teams_moved_down"]
        if ("moved_down_to_level" in promotion_relegation):
            self.moved_down_to_level = promotion_relegation["moved_down_to_level"]

    def get_all_matches(self):
        return self.matches

    def get_matches_by_date(self, date):
        return [match for match in self.matches if match.start_time.date() == date]

    def get_matches_by_team(self, team):
        return [match for match in self.matches if team in [match.home_team, match.away_team]]

    def to_dict(self):
        #print(self.matches)
        print(self.playoff_for_league)
        if self.playoff_for_league is None:
            playoff_name = None
        else:
            playoff_name = self.playoff_for_league.name
        return {
            'name': self.name,
            'country': self.country,
            'team_type': self.team_type,
            'level': self.level,
            'league_type': self.league_type,
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
            'playoff_name': playoff_name,
            'is_started': self.is_started,
            'num_teams_to_playoff': self.num_teams_to_playoff,
            'promotion_relegation':{
                'qualification_league_up': self.qualification_league_up,
                'qualification_league_down': self.qualification_league_down,
                'num_teams_moved_up': self.num_teams_moved_up,
                'moved_up_to_level': self.moved_up_to_level,
                'num_teams_to_qualification_up': self.num_teams_to_qualification_up,
                'num_teams_to_qualification_down': self.num_teams_to_qualification_down,
                'num_teams_moved_down': self.num_teams_moved_down,
                'moved_down_to_level': self.moved_down_to_level
            },
            'matches': [match.to_dict() for match in self.matches],
        }

    def calculate_table(self):
        #print(f"***************************")
        #print(f"|                         |")
        #print(f"|  Calculate table        |")
        #print(f"|    {self.name}       |")
        #print(f"|                         |")
        #print(f"***************************")
        #print(f"\n{self.table}\n\n")

        self.table = {team: {'played': 0, 'won': 0, 'drawn': 0, 'lost': 0, 'goals_for': 0, 'goals_against': 0, 'points': 0} for team in self.teams}

        #for team in self.table:
        #    print(f"team: {team}")
        #    self.table[team] = {'played': 0, 'won': 0, 'drawn': 0, 'lost': 0, 'goals_for': 0, 'goals_against': 0, 'points': 0}
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

    def get_playoff_teams(self):
        # Sort the table by points and goal difference
        sorted_table = sorted(self.table.items(), key=lambda x: (x[1]['points'], x[1]['goals_for'] - x[1]['goals_against']), reverse=True)

        # Get the top self.num_teams_to_playoff teams
        top_teams = [team[0] for team in sorted_table[:self.num_teams_to_playoff]]

        return top_teams

    def get_teams_to_move_down(self):
        sorted_table = sorted(self.table.items(), key=lambda x: (x[1]['points'], x[1]['goals_for'] - x[1]['goals_against']), reverse=False)
        return [team[0] for team in sorted_table[:self.num_teams_moved_down]]

    def get_teams_to_qualification_down(self):
        sorted_table = sorted(self.table.items(), key=lambda x: (x[1]['points'], x[1]['goals_for'] - x[1]['goals_against']), reverse=False)
        teams_to_move_down = self.get_teams_to_move_down()
        return [team[0] for team in sorted_table[self.num_teams_moved_down:self.num_teams_moved_down+self.num_teams_to_qualification_down] if team[0] not in teams_to_move_down]

    def get_teams_to_move_up(self):
        sorted_table = sorted(self.table.items(), key=lambda x: (x[1]['points'], x[1]['goals_for'] - x[1]['goals_against']), reverse=True)
        return [team[0] for team in sorted_table[:self.num_teams_moved_up]]

    def get_teams_to_qualification_up(self):
        sorted_table = sorted(self.table.items(), key=lambda x: (x[1]['points'], x[1]['goals_for'] - x[1]['goals_against']), reverse=True)
        teams_to_move_up = self.get_teams_to_move_up()
        return [team[0] for team in sorted_table[self.num_teams_moved_up:self.num_teams_moved_up+self.num_teams_to_qualification_up] if team[0] not in teams_to_move_up]


    def print_schedule(self):
        for match in self.matches:
            print(f"{match.year}-{match.month}-{match.day}: {match.home_team} vs. {match.away_team}")
        #for i, round in enumerate(self.rounds):
        #    print(f"Round {i + 1}:")
        #    for game in round:
        #        print(f"{game.home_team} vs. {game.away_team}")

    def is_completed(self):
        return all(match.played for match in self.matches)

