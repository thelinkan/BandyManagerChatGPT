from team import Team
from match import Match
from country import Country

class League:
    def __init__(self, name, country, level,teams , num_rounds=2, win_points=2, draw_points=1, start_month=11, start_day=1, end_month=2, end_day=15):
        self.name = name
        self.country = country
        self.num_teams = len(teams)
        self.num_rounds = num_rounds
        self.win_points = win_points
        self.draw_points = draw_points
        self.teams = teams
        self.matches = []
        self.table = {team: {'played': 0, 'won': 0, 'drawn': 0, 'lost': 0, 'goals_for': 0, 'goals_against': 0, 'points': 0} for team in teams}
        self.rounds = []
        self.generate_schedule()

    def generate_schedule(self):
        # Round-robin scheduling
        for round in range(self.num_rounds):
            round_matches = []
            for i in range(self.num_teams):
                for j in range(i + 1, self.num_teams):
                    home_team = self.teams[i]
                    away_team = self.teams[j]
                    round_matches.append(Match(home_team, away_team))
            self.rounds.append(round_matches)

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