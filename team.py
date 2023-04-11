import json
#from person import Player

class Team:
    def __init__(self, name, team_type,team_rating,num_players,num_int_players):
        self.name = name
        self.team_type = team_type
        self.rating = team_rating
        self.players = []
        self.num_players = num_players
        self.num_int_players = num_int_players

    def return_name(self):
        return self.name

    def return_team_type(self):
        return self.team_type

    def to_dict(self):
        return {
            'name': self.name,
            'team_type': self.team_type,
            'team_rating': self.rating,
            'num_players': 0,
            'num_int_players': 0,
            'players': [str(player.uuid) for player in self.players],
        }

    def print_players(self):
        print(f"Players in team {self.name}:")
        for player in self.players:
            print(f"- {player.first_name} {player.last_name} ({player.position})")

    def add_player(self, player):
        player.add_team(self)
        self.players.append(player)

    def return_num_players(self):
        return num_players,num_int_players

    def return_position(self):
        postion=self.player.return_position()
        return postion
