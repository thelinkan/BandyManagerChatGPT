from matchcode.match import Match
from country import Country

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
        self.rounds = {}  # initialize an empty dictionary to hold the playoff rounds
        league.playoff_for_league = self  # Set the `playoff_for_league` variable for the league�
        self.is_playoff = True

    def create_quarter_finals_schedule(self, top_teams):
        """Create the quarter finals schedule for the given top teams."""
        # Sort the top teams by their ranking (based on their performance in the league)
        top_teams = sorted(top_teams, key=lambda team: self.league.table[team]['points'], reverse=True)
        self.teams = top_teams
        # Determine the number of quarter finals matches
        num_matches = len(top_teams) // 2
        date_list = [[2024,2,15],[2024,2,18],[2024,2,21],[2024,2,24],[2024,2,27]]
        self.is_started = True
        round_matches = []  # create an empty list to hold the quarterfinals matches for this round
        # Create the quarter finals matches
        for i in range(num_matches):
            series_matches = []
            date = date_list[0]
            r_year = date[0]
            r_month = date[1]
            r_day = date[2]
            # Determine the home and away teams for the match
            home_team = top_teams[i]
            away_team = top_teams[-(i+1)]
            series = f"Quarterfinal {i+1}"
            print(f"Series: {series}")
            self.rounds[series] = {"home_team": home_team, "away_team": away_team, "matches": []}
            print(f"game {i}: {home_team.name} - {away_team.name}")
            match = Match(home_team,away_team,r_year,r_month,r_day)
            self.rounds[series]["matches"].append(match)
            self.matches.append(match)
            series_matches.append(match)  # add the match to the list for this round
            if self.match_manager is not None:
                self.match_manager.add_match(match,self)
            # Alternate home and away teams for the number of rounds
            for j in range(self.quarter_final_rounds - 1):
                date = date_list[j+1]
                r_year = date[0]
                r_month = date[1]
                r_day = date[2]
                home_team, away_team = away_team, home_team
                match = Match(home_team,away_team,r_year,r_month,r_day)
                self.matches.append(match)
                self.rounds[series]["matches"].append(match)
                #series_matches.append(match)  # add the match to the list for this round
                if self.match_manager is not None:
                    self.match_manager.add_match(match,self)

        #self.rounds['quarterfinals'] = round_matches  # add the list of quarterfinals matches to the rounds dictionary with the key 'quarterfinals'
        print(self.rounds)

    def check_elimination_quarterfinal(self, team1, team2):
        # Determine the number of matches needed to win the series
        if self.quarter_final_rounds == 5:
            matches_needed = 3
        elif self.quarter_final_rounds == 3:
            matches_needed = 2
        else:
            matches_needed = 1

        # Get the matches between the two teams
        matches = [match for match in self.matches if match.home_team in [team1, team2] and match.away_team in [team1, team2]]

        # Count the number of matches won by each team
        team1_wins = sum(1 for match in matches if match.winner() == team1)
        team2_wins = sum(1 for match in matches if match.winner() == team2)

        #print(f"    -    {self.name}: testing {team1.name} - {team2.name} __ {team1_wins} - {team2_wins} __Matches Needed: {matches_needed}")
        #for match in matches:
        #    print(f"    -    {match.home_goals} - {match.away_goals} Winner: {match.winner()}")
        # Check if one of the teams has already won enough matches
        if team1_wins >= matches_needed:
            # Delete the remaining matches between the two teams
            #self.matches = [match for match in self.matches if not (match.home_team == team1 and match.away_team == team2) and not (match.home_team == team2 and match.away_team == team1)]
            for match in self.matches:
                if (match.home_team == team1 and match.away_team == team2) or  (match.home_team == team2 and match.away_team == team1):
                    #print (f"      -      eliminating : {match.away_team.name} <--> {match.away_team.name}")
                    match.played = True
            #print(f"    -    team1 elimitates team 2")
            return team1
        elif team2_wins >= matches_needed:
            # Delete the remaining matches between the two teams
            #self.matches = [match for match in self.matches if not (match.home_team == team1 and match.away_team == team2) and not (match.home_team == team2 and match.away_team == team1)]
            for match in self.matches:
                if (match.home_team == team1 and match.away_team == team2) or  (match.home_team == team2 and match.away_team == team1):
                    match.played = True
                    #print (f"      -      eliminating : {match.home_team.name} <--> {match.away_team.name}")
            #print(f"    -    team2 elimitates team 1")
            return team2

        # No team has won enough matches yet
        return None

    def to_dict(self):
        return {
            'name': self.name,
            'country': self.country,
            'quarter_final_rounds': self.quarter_final_rounds,
            'semi_final_rounds': self.semi_final_rounds,
            'final_rounds': self.final_rounds,
            'is_started': self.is_started,

        }
