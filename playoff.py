class Playoff:
    def __init__(self, name, country, quarter_final_rounds, semi_final_rounds, final_rounds, league, match_manager):
        self.name = name
        self.country = country
        self.teams = []
        self.matches = []
        self.quarter_final_rounds = quarter_final_rounds
        self.semi_final_rounds = semi_final_rounds
        self.final_rounds = final_rounds
        self.league = league
        self.match_manager = match_manager
        self.is_started = False
        league.playoff_for_league = self  # Set the `playoff_for_league` variable for the league

    def create_quarter_finals_schedule(self, top_teams):
        """Create the quarter finals schedule for the given top teams."""
        # Sort the top teams by their ranking (based on their performance in the league)
        top_teams = sorted(top_teams, key=lambda team: self.league.table[team]['points'], reverse=True)

        # Determine the number of quarter finals matches
        num_matches = len(top_teams) // 2

        # Create the quarter finals matches
        for i in range(num_matches):
            # Determine the home and away teams for the match
            home_team = top_teams[i]
            away_team = top_teams[-(i+1)]
            print(f"game {i}: {home_team.name} - {away_team.name}")

        #    # Create the match
        #    match = Match(home_team, away_team, self.country, self.name)

        #    # Add the match to the playoff and the match manager
        #    self.matches.append(match)
        #    self.match_manager.add_match(match, self)

        #    # Alternate home and away teams for the number of rounds
        #    for j in range(self.quarter_final_rounds - 1):
        #        home_team, away_team = away_team, home_team
        #        match = Match(home_team, away_team, self.country, self.name)
        #        self.matches.append(match)
        #        self.match_manager.add_match(match, self)
        
    def to_dict(self):
        return {
            'name': self.name,
            'country': self.country,
            'quarter_final_rounds': self.quarter_final_rounds,
            'semi_final_rounds': self.semi_final_rounds,
            'final_rounds': self.final_rounds,
            'is_started': self.is_started,
            
        }
