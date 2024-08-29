import json
import random
import ast
import uuid
#from person import Player

class Team:
    def __init__(self, name, team_type,team_rating,num_players,num_int_players, jersey_colors, jersey_decorations, club):
        self.name = name
        self.team_type = team_type
        self.rating = team_rating
        self.players = {}
        self.num_players = num_players
        self.num_int_players = num_int_players
        self.jersey_colors = ast.literal_eval(jersey_colors)
        self.jersey_decorations = ast.literal_eval(jersey_decorations)
        self.club = club
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
        '''
        Passing:
            Longballs 0 = Never, 10 = always
        Defense:
            type - 0 = neutral, 1 = high pressure, 2 = park the buss, 3 = "Garbage bag"
        Offense:
            type - 0 = neutral, 1 = value and slow advance, 2 = offensive, 3 = counter-attack
        Corner:
            cornertaker: uuid, targetplayers 1-4 uuid
        freestroke:
            targetplayers: 1-3 uuid
        '''
        self.tactics = {
            "passing": {"longballs": 3},
            "defence": {"type":0},
            "offence": {"type":0},
            "corner": {"cornertaker": 0, "targetplayers": [1,2,3, 4]},
            "freestroke": {"targetplayers": [1,2,3]}
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
            'jersey_decorations': str(self.jersey_decorations),
            'tactics': {
                'passing': {'longballs': self.tactics['passing']['longballs']},
                'defence': {'type': self.tactics['defence']['type']},
                'offence': {'type': self.tactics['offence']['type']},
                'corner': {'cornertaker': self.tactics['corner']['cornertaker'], 'targetplayers':  self.tactics['corner']['targetplayers']},
                'freestroke': {'targetplayers': self.tactics['freestroke']['targetplayers']}
            }
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

    def get_players_positions(self):
        player_position_list = []
        for position, position_data in self.actual_positions.items():
            player_uuid = position_data["player_uuid"]
            if player_uuid is not None and player_uuid in self.players:
                player = self.players[player_uuid]
                player_position_list.append(
                    (player.uuid, player.jersey_number, player.first_name, player.last_name, player.age, player.position, position)
                )
        return player_position_list

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

    def change_player_jersey_number(self, player_uuid : uuid.UUID, new_jersey_number: int):
        '''
        Change the Jersey number of the player with uuid player_uuid
        '''
        # Check if jersey number is between 1 and 99
        #print (new_jersey_number)
        if new_jersey_number < 1 or new_jersey_number > 99:
            print("Jersey number must be between 1 and 99.")
            return False

        # Check if no other player has the same jersey number
        #print(self.players)
        for player_uuid_keys in self.players.keys():
            #print(self.players[player_uuid].jersey_number)
            if self.players[player_uuid_keys].jersey_number == new_jersey_number and str(self.player.uuid) != str(player_uuid):

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
        # Categorize players by their broad position
        position_groups = {
            "goalkeeper": [],
            "defender": [],
            "half back": [],
            "midfielder": [],
            "forward": []
        }

        # Assign players to position groups based on their position
        for player_uuid in self.players:
            player = self.players[player_uuid]
            if player.position in position_groups:
                position_groups[player.position].append(player.uuid)
            else:
                position_groups["forward"].append(player.uuid)  # default to forward if unspecified

        # Shuffle each group of players to randomize assignments
        for group in position_groups.values():
            random.shuffle(group)

        # Helper function to assign players to positions, filling from other groups if needed
        def assign_position(position_name, required_group):
            if position_groups[required_group]:
                self.actual_positions[position_name]["player_uuid"] = position_groups[required_group].pop(0)
            else:
                # If the required group is empty, fill from any available group
                for group_name in position_groups:
                    if position_groups[group_name]:
                        self.actual_positions[position_name]["player_uuid"] = position_groups[group_name].pop(0)
                        break
                else:
                    self.actual_positions[position_name]["player_uuid"] = None

        # Assign players to their corresponding positions
        # Goalkeeper
        assign_position("goalkeeper", "goalkeeper")

        # Defenders
        for position in ["libero", "leftdef", "rightdef"]:
            assign_position(position, "defender")

        # Halfbacks
        for position in ["lefthalf", "righthalf"]:
            assign_position(position, "half back")

        # Midfielders
        for position in ["leftmid", "centralmid", "rightmid"]:
            assign_position(position, "midfielder")

        # Attackers
        for position in ["leftattack", "rightattack"]:
            assign_position(position, "forward")

        # Fill substitutes
        subs = []
        
        # 1 goalkeeper as sub if available
        if position_groups["goalkeeper"]:
            subs.append(position_groups["goalkeeper"].pop(0))

        # 1-2 defenders/halfbacks
        for _ in range(2):
            if len(subs) >= 5:
                break
            for group_name in ["defender", "half back"]:
                if position_groups[group_name]:
                    subs.append(position_groups[group_name].pop(0))
                    break
        
        # 1-2 midfielders
        for _ in range(2):
            if len(subs) >= 5:
                break
            if position_groups["midfielder"]:
                subs.append(position_groups["midfielder"].pop(0))
        
        # 1-2 forward
        for _ in range(2):
            if len(subs) >= 5:
                break
            if position_groups["forward"]:
                subs.append(position_groups["forward"].pop(0))

        # Fill remaining sub slots if any, from any available player
        while len(subs) < 5:
            for group_name in position_groups:
                if position_groups[group_name]:
                    subs.append(position_groups[group_name].pop(0))
                    break
            else:
                break

        # Assign substitutes to sub positions
        for i in range(5):
            sub_position = f"sub{i + 1}"
            self.actual_positions[sub_position]["player_uuid"] = subs[i] if i < len(subs) else None


        self.tactics['corner']['cornertaker'] = self.actual_positions["centralmid"]["player_uuid"]

        while len(self.tactics['corner']['targetplayers']) < 4:
            self.tactics['corner']['targetplayers'].append(None)  # Append a placeholder value
        
        self.tactics['corner']['targetplayers'][0] = self.actual_positions["leftattack"]["player_uuid"]
        self.tactics['corner']['targetplayers'][1] = self.actual_positions["rightattack"]["player_uuid"]
        self.tactics['corner']['targetplayers'][2] = self.actual_positions["leftmid"]["player_uuid"]
        self.tactics['corner']['targetplayers'][3] = self.actual_positions["rightmid"]["player_uuid"]

        while len(self.tactics['freestroke']['targetplayers']) < 3:
            self.tactics['freestroke']['targetplayers'].append(None)        

        self.tactics['freestroke']['targetplayers'][0] = self.actual_positions["rightattack"]["player_uuid"]
        self.tactics['freestroke']['targetplayers'][1] = self.actual_positions["leftattack"]["player_uuid"]
        self.tactics['freestroke']['targetplayers'][2] = self.actual_positions["centralmid"]["player_uuid"]
