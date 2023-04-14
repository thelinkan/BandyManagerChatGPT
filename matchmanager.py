import datetime as dt

class MatchManager:
    def __init__(self):
        self.matches = []

    def add_match(self, match, league):
        match.league = league
        self.matches.append(match)

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
