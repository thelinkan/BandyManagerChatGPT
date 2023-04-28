import datetime as dt

class MatchManager:
    def __init__(self):
        self.matches = []
        self.leagues = []

    def add_match(self, match, league):
        match.league = league
        self.matches.append(match)
        if league not in self.leagues:
            self.leagues.append(league)

    def get_all_matches(self):
        return self.matches

    def get_next_match_for_team(self, team_name, year, month, day):
        now = dt.datetime(year, month, day)
        matches = [match for match in self.matches if not match.played and dt.datetime(match.year, match.month, match.day) >= now and (match.home_team.name == team_name or match.away_team.name == team_name)]
        if matches:
            return min(matches, key=lambda match: dt.datetime(match.year, match.month, match.day))
        else:
            return None

    def get_matches_by_date(self, year, month, day):
        date = dt.datetime(year, month, day)
        matches = [match for match in self.matches if dt.datetime(match.year, match.month, match.day) == date]
        return matches

    def get_matches_by_league(self, league_name):
        league_matches = [match for match in self.matches if match.league.name == league_name]
        sorted_matches = sorted(league_matches, key=lambda match: dt.date(match.year, match.month, match.day))
        return sorted_matches

    def get_league_of_match(self, match):
        return match.league

    def play_viewed_match(self,match):
        time_scaling_factor = 0.1875
        if(match.played == False):
            start_time = time.time()
            match.played = True
            game_time = 0
        current_time = time.time()
        elapsed_time = current_time - start_time
        game_time_delta = elapsed_time * time_scaling_factor
        game_time += game_time_delta

