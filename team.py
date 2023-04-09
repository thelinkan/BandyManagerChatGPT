import json

class Team:
    def __init__(self, name, team_type,team_rating):
        self.name = name
        self.team_type = team_type
        self.rating = team_rating

    def return_name(self):
        return self.name
        
    def to_dict(self):
        return {
            'name': self.name,
            'team_type': self.team_type,
            'team_rating': self.rating,
            'num_players': 0,
            'num_int_players': 0

        }
