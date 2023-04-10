import uuid
import weakref
#from team import Team

class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

class Player(Person):
    def __init__(self, first_name, last_name, age, gender, position, team):
        super().__init__(first_name, last_name, age, gender)
        self.position = position
        self.team = team
        self.uuid = uuid.uuid4()
        self.team_ref = None

    def add_team(self, team):
        self.team_ref = weakref.ref(team)

    def to_dict(self):
        player_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'gender': self.gender,
            'position': self.position,
            'uuid': str(self.uuid),
            'teams': [team.name for team in self.teams]  # Include only the team names
        }
        return player_dict
        
    def return_position(self):
        return self.position

    def __str__(self):
        return f"Player first name: {self.first_name} last name: {self.last_name} age: {self.age}"

class Referee(Person):
    def __init__(self, first_name, last_name, age, gender, level):
        super().__init__(first_name, last_name, age, gender)
        self.level = level

class ClubStaff(Person):
    def __init__(self, first_name, last_name, age, gender, role, team):
        super().__init__(first_name, last_name, age, gender)
        self.role = role
        self.team = team
        
class PlayerManager:
    def __init__(self):
        self.players = []
        
    def add_player(self, player):
        self.players.append(player)
        
    def remove_player(self, player):
        self.players.remove(player)
        
    def find_player_by_id(self, player_id):
        for player in self.players:
            if player.id == player_id:
                return player
        return None
        
    def find_players_by_name(self, name):
        return [player for player in self.players if player.name == name]
    
    def find_players_by_age_range(self, min_age, max_age):
        return [player for player in self.players if min_age <= player.age <= max_age]
    
    def find_players_by_gender(self, gender):
        return [player for player in self.players if player.gender == gender]
        
    def print_players(self):
        for player in self.players:
            print(player)

    def create_player(self, first_name, last_name, age, gender, position, team):
        player = Player(first_name, last_name, age, gender, position, team)
        self.players.append(player)
        return player