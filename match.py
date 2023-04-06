class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = 0
        self.away_goals = 0
        self.played = False

    def play(self):
        home_strength = self.home_team.strength()
        away_strength = self.away_team.strength()
        home_goals = np.random.poisson(home_strength)
        away_goals = np.random.poisson(away_strength)
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.home_team.played(self, home_goals, away_goals)
        self.away_team.played(self, away_goals, home_goals)
        self.played = True
