import json
from team import Team

class Club:
    def __init__(self, name: str, country, rating: int, home_arena: str, logo: str|None):
        self.name:str = name
        self.country = country
        self.rating :int = rating
        self.home_arena:str = home_arena
        self.logo: str|None = logo
        self.teams: list[Team] = []

    def add_team(self, team: Team):
        self.teams.append(team)

    def get_teams_by_type(self, team_type: str) -> list[Team]:
        return [team for team in self.teams if team.team_type == team_type]

    def to_dict(self) -> dict:
        '''
        Return a dict of the club, including all the teams
        '''
        teams_data =[]
        for team in self.teams:
            teams_data.append(team.to_dict())
        return {
            'name': self.name,
            'country': self.country,
            'club_rating': self.rating,
            'home_arena': self.home_arena,
            'logo': self.logo,
            'teams': teams_data
        }