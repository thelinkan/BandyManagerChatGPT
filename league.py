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


        #matches_per_round = n // 2

        # Make a list of all the possible matches
        #possible_matches = [(self.teams[i], self.teams[j]) for i in range(n) for j in range(i+1, n)]
        #for match in possible_matches:
        #    print(f"{match[0].name} vs {match[1].name}")
        #print(possible_matches)
        # Loop through each round
        #for round_num in range(rounds):
        #        # Shuffle the list of possible matches to randomize the schedule
        #    random.shuffle(possible_matches)

        #    # Make a list of matches for this round
        #    matches_this_round = []

        #    # Loop through each match for this round
        #    for match_num in range(matches_per_round):
        #        # Get the next available match from the list of possible matches
        #        match = possible_matches.pop(0)

        #        # Check if either team is already playing in this round
        #        if any(match[0] in m or match[1] in m for m in matches_this_round):
        #            # If so, put the match back into the list of possible matches
        #            possible_matches.append(match)
        #        else:
        #            # Otherwise, add the match to the list of matches for this round
        #            matches_this_round.append(match)

        #    # Add the matches for this round to the schedule
        #    self.schedule.append(matches_this_round)

    #def generate_schedule(self):
    #    # Round-robin scheduling
    #    for round in range(self.num_rounds):
    #        round_matches = []
    #        for i in range(self.num_teams):
    #            for j in range(i + 1, self.num_teams):
    #                home_team = self.teams[i]
    #                away_team = self.teams[j]
    #                round_matches.append(Match(home_team, away_team))
    #        self.rounds.append(round_matches)

    #def play_round(self, round_number):
    #    for game in self.rounds[round_number]:
    #        game.play()
    #        home_team = game.home_team
    #        away_team = game.away_team
    #        self.table[home_team]['played'] += 1
    #        self.table[away_team]['played'] += 1
    #        self.table[home_team]['goals_for'] += game.home_score
    #        self.table[away_team]['goals_for'] += game.away_score
    #        self.table[home_team]['goals_against'] += game.away_score
    #        self.table[away_team]['goals_against'] += game.home_score
    #        if game.home_score > game.away_score:
    #            self.table[home_team]['won'] += 1
    #            self.table[home_team]['points'] += self.win_points
    #            self.table[away_team]['lost'] += 1
    #        elif game.home_score < game.away_score:
    #            self.table[away_team]['won'] += 1
    #            self.table[away_team]['points'] += self.win_points
    #            self.table[home_team]['lost'] += 1
    #        else:
    #            self.table[home_team]['drawn'] += 1
    #            self.table[home_team]['points'] += self.draw_points
    #            self.table[away_team]['drawn'] += 1
    #            self.table[away_team]['points'] += self.draw_points
    #        self.games.append(game)

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