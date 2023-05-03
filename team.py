import json
import random
import ast
#from person import Player

class Team:
    def __init__(self, name, team_type,team_rating,num_players,num_int_players, jersey_colors, jersey_decorations):
        self.name = name
        self.team_type = team_type
        self.rating = team_rating
        self.players = {}
        self.num_players = num_players
        self.num_int_players = num_int_players
        self.jersey_colors = ast.literal_eval(jersey_colors)
        self.jersey_decorations = ast.literal_eval(jersey_decorations)
        print(f"{self.name} - {self.jersey_decorations}")
        self.actual_positions = {
            "goalkeeper": {"player_uuid": None, "tactic": 0},
            "libero": {"player_uuid": None, "tactic": 0},
            "leftdef": {"player_uuid": None, "tactic": 0},
            "rightdef": {"player_uuid": None, "tactic": 0},
            "lefthalf": {"player_uuid": None, "tactic": 0},
            "righthalf": {"player_uuid": None, "tactic": 0},
            "leftmid": {"player_uuid": None, "tactic": 0},
            "centralmid": {"player_uuid": None, "tactic": 0},
            "rightmid": {"player_uuid": None, "tactic": 0},
            "leftattack": {"player_uuid": None, "tactic": 0},
            "rightattack": {"player_uuid": None, "tactic": 0},
            'sub1': {'player_uuid': None, 'tactic': 0},
            'sub2': {'player_uuid': None, 'tactic': 0},
            'sub3': {'player_uuid': None, 'tactic': 0},
            'sub4': {'player_uuid': None, 'tactic': 0},
            'sub5': {'player_uuid': None, 'tactic': 0}
        }

    def return_name(self):
        return self.name

    def return_jersey_colors(self):
        return self.jersey_colors

    def return_jersey_decorations(self):
        return self.jersey_decorations

    def return_team_type(self):
        return self.team_type

    def to_dict(self):
        player_list = []
        for player_uuid in self.players.keys():
            player_dict = {
                'uuid': str(player_uuid),
                'jersey_number': self.players[player_uuid].jersey_number
            }
            player_list.append(player_dict)
        position_list = []
        for actual_position in self.actual_positions.keys():
            position_dict = {
                'actual_position': actual_position,
                'player_uuid': str(self.actual_positions[actual_position]['player_uuid']),
                'tactic': self.actual_positions[actual_position]['tactic']
            }
            position_list.append(position_dict)
            
        #print(self.players)
        return {
            'name': self.name,
            'team_type': self.team_type,
            'team_rating': self.rating,
            'num_players': 0,
            'num_int_players': 0,
            'players': player_list,
            'actual_positions': position_list,
            'jersey_colors': str(self.jersey_colors),
            'jersey_decorations': str(self.jersey_decorations)
        }

    def print_players(self):
        print(f"Players in team {self.name}:")
        for player_uuid in self.players:
            #print(f"- {self.player[player.uuid].jersey_number}  {player.first_name} {player.last_name} ({player.position})")
            print(f"- {self.players[player_uuid].jersey_number}")

    def get_players(self):
        player_list = []
        for player in self.players.values():
            player_list.append((player.uuid, self.players[player.uuid].jersey_number, player.first_name, player.last_name, player.age, player.position))
        return player_list

    def add_player(self, player):
        player.add_team(self)
        self.players[player.uuid] = player
        self.players[player.uuid].jersey_number = 0
        #self.players.append(player)

    def return_num_players(self):
        return self.num_players,self.num_int_players

    def return_position(self):
        postion=self.player.return_position()
        return postion

    def change_player_jersey_number(self, player_uuid, new_jersey_number):
        # Check if jersey number is between 1 and 99
        #print (new_jersey_number)
        if new_jersey_number < 1 or new_jersey_number > 99:
            print("Jersey number must be between 1 and 99.")
            return False

        # Check if no other player has the same jersey number
        #print(self.players)
        for player_uuid in self.players.keys():
            #print(self.players[player_uuid].jersey_number)
            if self.players[player_uuid].jersey_number == new_jersey_number and str(self.player.uuid) != str(player_uuid):
                print(f"Player {self.player.first_name} {self.player.last_name} already has jersey number {new_jersey_number}.")
                return False

        # Add or change the jersey number in the players dictionary
        if player_uuid in self.players:
            self.players[player_uuid].jersey_number = new_jersey_number
            return True
        else:
            print(f"Player with UUID {player_uuid} not found in team {self.name}.")
            return False
    
    def assign_player_to_position(self,position,position_uuid):
        # Create a list of player UUIDs
        player_uuids = list(self.players.keys())
        
        assign_uuid = None
        
        for player_uuid in player_uuids:
            if str(player_uuid) == str(position_uuid):
                assign_uuid = player_uuid
        
        if assign_uuid is not None:
            self.actual_positions[position]["player_uuid"] = assign_uuid

    def assign_players_to_positions(self):
        # Create a list of player UUIDs
        player_uuids = list(self.players.keys())

        # Shuffle the list of player UUIDs
        random.shuffle(player_uuids)

        # Assign each position to a player UUID
        self.actual_positions["goalkeeper"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["libero"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["leftdef"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["rightdef"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["lefthalf"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["righthalf"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["leftmid"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["centralmid"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["rightmid"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["leftattack"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["rightattack"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["sub1"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["sub2"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["sub3"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["sub4"]["player_uuid"] = player_uuids.pop(0)
        self.actual_positions["sub5"]["player_uuid"] = player_uuids.pop(0)
                
                