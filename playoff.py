from matchcode.match import Match
from country import Country
from debug_functions import print_playoff_series

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
        self.rounds["Quarterfinals"] = {"is_completed": False, "is_scheduled": True}
        self.rounds["Semifinals"] = {"is_completed": False, "is_scheduled": False}
        self.rounds["Finals"] = {"is_completed": False, "is_scheduled": False}
        # Create the quarter finals matches
        for i in range(num_matches):
            date = date_list[0]
            r_year = date[0]
            r_month = date[1]
            r_day = date[2]
            # Determine the home and away teams for the match
            home_team = top_teams[i]
            away_team = top_teams[-(i+1)]
            series = f"Quarterfinal {i+1}"
            print(f"Series: {series}")
            self.rounds["Quarterfinals"][series] = {"home_team": home_team, "away_team": away_team, "home_team_wins": 0, "away_team_wins": 0, "winner_team": None, "matches": []}
            print(f"game {i}: {home_team.name} - {away_team.name}")
            match = Match(home_team,away_team,r_year,r_month,r_day)
            self.rounds["Quarterfinals"][series]["matches"].append(match)
            self.matches.append(match)
            #series_matches.append(match)  # add the match to the list for this round
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
                self.rounds["Quarterfinals"][series]["matches"].append(match)
                #series_matches.append(match)  # add the match to the list for this round
                if self.match_manager is not None:
                    self.match_manager.add_match(match,self)

        #self.rounds['quarterfinals'] = round_matches  # add the list of quarterfinals matches to the rounds dictionary with the key 'quarterfinals'
        #print("self.rounds")
        #print(self.rounds)

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

        qfinals = ["Quarterfinal 1","Quarterfinal 2","Quarterfinal 3","Quarterfinal 4"]
        for qfinal in qfinals:
            if(self.rounds["Quarterfinals"][qfinal]["home_team"] == team1 and self.rounds["Quarterfinals"][qfinal]["away_team"] == team2):
                self.rounds["Quarterfinals"][qfinal]["home_team_wins"]=team1_wins
                self.rounds["Quarterfinals"][qfinal]["away_team_wins"]=team2_wins
                if team1_wins >= matches_needed:
                    self.rounds["Quarterfinals"][qfinal]["winner_team"]=team1
                if team2_wins >= matches_needed:
                    self.rounds["Quarterfinals"][qfinal]["winner_team"]=team2
                print(qfinal)
                print_playoff_series(self.rounds["Quarterfinals"][qfinal])
            if(self.rounds["Quarterfinals"][qfinal]["home_team"] == team2 and self.rounds["Quarterfinals"][qfinal]["away_team"] == team1):
                self.rounds["Quarterfinals"][qfinal]["home_team_wins"]=team2_wins
                self.rounds["Quarterfinals"][qfinal]["away_team_wins"]=team1_wins
                if team1_wins >= matches_needed:
                    self.rounds["Quarterfinals"][qfinal]["winner_team"]=team1
                if team2_wins >= matches_needed:
                    self.rounds["Quarterfinals"][qfinal]["winner_team"]=team2
                print(qfinal)
                print_playoff_series(self.rounds["Quarterfinals"][qfinal])

        # Check if one of the teams has already won enough matches
        if team1_wins >= matches_needed:
            # Delete the remaining matches between the two teams
            for match in self.matches:
                if (match.home_team == team1 and match.away_team == team2) or  (match.home_team == team2 and match.away_team == team1):
                    match.played = True
            return team1
        elif team2_wins >= matches_needed:
            # Delete the remaining matches between the two teams
            for match in self.matches:
                if (match.home_team == team1 and match.away_team == team2) or  (match.home_team == team2 and match.away_team == team1):
                    match.played = True
            return team2

        # No team has won enough matches yet
        return None

    def check_quarterfinals_completed(self):
        qfinals = ["Quarterfinal 1","Quarterfinal 2","Quarterfinal 3","Quarterfinal 4"]
        if(self.is_started):
            quarterfinals_completed = self.rounds["Quarterfinals"]["is_completed"]
            if not quarterfinals_completed:
                quarterfinals_completed = True
                for qfinal in qfinals:
                    if self.rounds["Quarterfinals"][qfinal]["winner_team"] is None:
                        quarterfinals_completed = False
                self.rounds["Quarterfinals"]["is_completed"] = quarterfinals_completed
            print(f"Test quarterfinals {self.name} - {quarterfinals_completed}")
            return quarterfinals_completed
        return False

    def create_semi_schedule_from_quarter(self):
        quarterfinals_completed = self.check_quarterfinals_completed()
        if quarterfinals_completed and not self.rounds["Semifinals"]["is_scheduled"]:
            self.rounds["Semifinals"]["is_scheduled"] = True
            team_list = []
            for i in range(4):
                qfinal = f"Quarterfinal {i+1}"
                team_list.append(self.rounds["Quarterfinals"][qfinal]["winner_team"])
            num_matches = 2
            date_list = [[2024,3,3],[2024,3,6],[2024,3,9],[2024,3,12],[2024,3,15]]
            for i in range(num_matches):
                date = date_list[0]
                r_year = date[0]
                r_month = date[1]
                r_day = date[2]
                # Determine the home and away teams for the match
                home_team = team_list[i]
                away_team = team_list[-(i+1)]
                series = f"Semifinal {i+1}"
                self.rounds["Semifinals"][series] = {"home_team": home_team, "away_team": away_team, "home_team_wins": 0, "away_team_wins": 0, "winner_team": None, "matches": []}
                match = Match(home_team,away_team,r_year,r_month,r_day)
                self.rounds["Semifinals"][series]["matches"].append(match)
                self.matches.append(match)
                if self.match_manager is not None:
                    self.match_manager.add_match(match,self)
                    for j in range(self.semi_final_rounds - 1):
                        date = date_list[j+1]
                        r_year = date[0]
                        r_month = date[1]
                        r_day = date[2]
                        home_team, away_team = away_team, home_team
                        match = Match(home_team,away_team,r_year,r_month,r_day)
                        self.matches.append(match)
                        self.rounds["Semifinals"][series]["matches"].append(match)
                        if self.match_manager is not None:
                            self.match_manager.add_match(match,self)
                print_playoff_series(self.rounds["Semifinals"][series])
            #print(self.rounds["Semifinals"])
           
    def check_semifinals_completed(self):
        sfinals = ["Semifinal 1","Semifinal 2"]
        if(self.is_started and self.rounds["Semifinals"]["is_scheduled"]):
            semifinals_completed = self.rounds["Semifinals"]["is_completed"]
            if not semifinals_completed:
                semifinals_completed = True
                for sfinal in sfinals:
                    if self.rounds["Semifinals"][sfinal]["winner_team"] is None:
                        semifinals_completed = False
                self.rounds["Semifinals"]["is_completed"] = semifinals_completed
            print(f"Test Semifinals {self.name} - {semifinals_completed}")
            return semifinals_completed
        return False
            
    def create_final_schedule_from_semi(self):
        semifinals_completed = self.check_semifinals_completed()
        if semifinals_completed and not self.rounds["Finals"]["is_scheduled"]:
            self.rounds["Finals"]["is_scheduled"] = True
            team_list = []
            for i in range(2):
                sfinal = f"Semifinal {i+1}"
                team_list.append(self.rounds["Semifinals"][sfinal]["winner_team"])
            num_matches = 1
            date_list = [[2024,3,22],[2024,3,25],[2024,3,28],[2024,4,1],[2024,4,4]]
            for i in range(num_matches):
                date = date_list[0]
                r_year = date[0]
                r_month = date[1]
                r_day = date[2]
                # Determine the home and away teams for the match
                home_team = team_list[i]
                away_team = team_list[-(i+1)]
                series = f"Final {i+1}"
                self.rounds["Finals"][series] = {"home_team": home_team, "away_team": away_team, "home_team_wins": 0, "away_team_wins": 0, "winner_team": None, "matches": []}
                match = Match(home_team,away_team,r_year,r_month,r_day)
                self.rounds["Finals"][series]["matches"].append(match)
                self.matches.append(match)
                if self.match_manager is not None:
                    self.match_manager.add_match(match,self)
                    for j in range(self.semi_final_rounds - 1):
                        date = date_list[j+1]
                        r_year = date[0]
                        r_month = date[1]
                        r_day = date[2]
                        home_team, away_team = away_team, home_team
                        match = Match(home_team,away_team,r_year,r_month,r_day)
                        self.matches.append(match)
                        self.rounds["Finals"][series]["matches"].append(match)
                        if self.match_manager is not None:
                            self.match_manager.add_match(match,self)
                print_playoff_series(self.rounds["Finals"][series])
            #print(self.rounds["Semifinals"])



    def to_dict(self):
        return {
            'name': self.name,
            'country': self.country,
            'quarter_final_rounds': self.quarter_final_rounds,
            'semi_final_rounds': self.semi_final_rounds,
            'final_rounds': self.final_rounds,
            'is_started': self.is_started,

        }
