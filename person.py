import uuid
import random
import weakref
from attribute import Attribute
#from team import Team

class Person:
    def __init__(self, first_name, last_name, age, gender, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.nationality = nationality

class Player(Person):
    def __init__(self, first_name, last_name, age, gender, nationality, position, team):
        super().__init__(first_name, last_name, age, gender, nationality)
        self.position = position
        self.team = team
        self.uuid = uuid.uuid4()
        self.team_ref = None
        self.attributes = [
            Attribute('Saveing', -1, 0),
            Attribute('Reflexes', -1, 0),
            Attribute('Placement', -1, 0),
            Attribute('Throwing', -1, 0),
            Attribute('Dribbling', -1, 0),
            Attribute('Corners', -1, 0),
            Attribute('Passing', -1, 0),
            Attribute('Long pass', -1, 0),
            Attribute('Shooting', -1, 0),
            Attribute('Skating', -1, 0),
            Attribute('Acceleration', -1, 0),
            Attribute('Agression', -1, 0),
            Attribute('Agility', -1, 0),
            Attribute('Endurance', -1, 0),
            Attribute('Condition', -1, 0)
        ]
 
    def generate_attributes(self, country_knowledge, gender_proficiency, club_rating, team_rating):
        for attribute in self.attributes:
            #generic attributes
            if attribute.name == "Endurance":
                age_scale = -0.3125 * self.age * self.age + 16.25 * self.age - 111.25
                attribute.level = round(random.randint(70,100)*age_scale/100)
            if attribute.name == "Agility":
                age_scale = -0.3125 * self.age * self.age + 16.25 * self.age - 111.25
                attribute.level = round(random.randint(70,100)*age_scale/100)
            if attribute.name == "Agression":
                mean = 70
                stddev = 15
                num = int(random.normalvariate(mean, stddev))
                #num = int(num * 10 + 70)
                attribute.level = min(max(num, 1), 100)
                #attribute.level = num
 
    def set_attribute(self, attribute_name,value,experience):
        for attribute in self.attributes:
            if attribute.name == attribute_name:
                attribute.level = value
                attribute.experience = experience
 
    def get_attribute(self, attribute_name):
        for attribute in self.attributes:
            if attribute.name == attribute_name:
                return attribute
        return None

    def add_team(self, team):
        self.team_ref = weakref.ref(team)

    def to_dict(self):
        attributes_dict = {attribute.name: attribute.to_dict() for attribute in self.attributes}
        player_dict = {
            'uuid': str(self.uuid),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'gender': self.gender,
            'nationality': self.nationality,
            'position': self.position,
            'team': self.team,
            'attributes': attributes_dict
            #'teams': [team.name for team in self.team_ref]  # Include only the team names
        }
        return player_dict

    def return_position(self):
        return self.position

    def return_skills(self):
        return self.skills
        
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

    def find_player_by_uuid(self, player_uuid):
        for player in self.players:
            if str(player.uuid) == str(player_uuid):
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
            print(player.uuid)

    def create_player(self, first_name, last_name, age, gender, nationality, position, team):
        player = Player(first_name, last_name, age, gender, nationality, position, team)
        self.players.append(player)
        return player

    def load_player(self, first_name, last_name, age, gender, nationality, position, team, uuidload):
        player = Player(first_name, last_name, age, gender, nationality, position, team)
        player.uuid = uuid.UUID(uuidload)
        self.players.append(player)
        return player

    #def from_list(cls, game, players_data):
    #    for player_data in players_data:
    #        player = Player(player_data['first_name'], player_data['last_name'], player_data['age'], player_data['gender'], player_data['position'], player_data['team'])
    #        player.uuid = uuid.UUID(player_data['uuid'])
    #        game.player_manager.add_player(player)

