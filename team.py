import json

class Team:
    def __init__(self, name, team_type):
        self.name = name
        self.team_type = team_type

    def return_name(self):
        return self.name
