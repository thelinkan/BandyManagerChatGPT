import json

class Club:
    def __init__(self, name, country, rating, home_arena):
        self.name = name
        self.country = country
        self.rating = rating
        self.home_arena = home_arena
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def get_teams_by_type(self, team_type):
        return [team for team in self.teams if team.team_type == team_type]

    def to_dict(self):
        teams_data =[]
        for team in self.teams:
            teams_data.append(team.to_dict())        
        return {
            'name': self.name,
            'country': self.country,
            'club_rating': self.rating,
            'home_arena': self.home_arena,
            'teams': teams_data
        }