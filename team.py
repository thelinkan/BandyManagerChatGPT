import json
import ast
#from person import Player

class Team:
    def __init__(self, name, team_type,team_rating,num_players,num_int_players, jersey_colors):
        self.name = name
        self.team_type = team_type
        self.rating = team_rating
        self.players = {}
        self.num_players = num_players
        self.num_int_players = num_int_players
        self.jersey_colors = ast.literal_eval(jersey_colors)

    def return_name(self):
        return self.name

    def return_jersey_colors(self):
        return self.jersey_colors

    def return_team_type(self):
        return self.team_type

    def to_dict(self):
        #print(self.players)
        return {
            'name': self.name,
            'team_type': self.team_type,
            'team_rating': self.rating,
            'num_players': 0,
            'num_int_players': 0,
            'players': [str(player_uuid) for player_uuid in self.players.keys()],
            'jersey_colors': str(self.jersey_colors)
        }

    def print_players(self):
        print(f"Players in team {self.name}:")
        for player in self.players:
            print(f"- {player.first_name} {player.last_name} ({player.position})")

    def get_players(self):
        player_list = []
        for player in self.players.values():
            player_list.append((player.uuid, player.first_name, player.last_name, player.age, player.position))
        return player_list

    def add_player(self, player):
        player.add_team(self)
        self.players[player.uuid] = player
        #self.players.append(player)

    def return_num_players(self):
        return num_players,num_int_players

    def return_position(self):
        postion=self.player.return_position()
        return postion
