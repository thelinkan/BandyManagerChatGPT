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
            Attribute('Intercept', -1, 0),
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
        total_rating = gender_proficiency * team_rating/10000
        #print (f"Team {total_rating} - {gender_proficiency} - {team_rating}")
        for attribute in self.attributes:
            #generic attributes
            if attribute.name == "Endurance":
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                attribute.level = round(random.randint(70,100)*age_scale)
            if attribute.name == "Agility":
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                attribute.level = round(random.randint(70,100)*age_scale)
            if attribute.name == "Agression":
                mean = 70
                stddev = 15
                num = int(random.normalvariate(mean, stddev))
                attribute.level = min(max(num, 1), 100)
            if attribute.name == "Condition":
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                attribute.level = round(random.randint(70,100)*age_scale)
            #skating attributes
            if attribute.name == "Skating":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(50,70)/100
                else:
                    pos_scale = random.randint(60,100)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                attribute.level = round(random.randint(70,100) * age_scale * total_rating  * pos_scale)
            if attribute.name == "Acceleration":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(30,50)/100
                elif self.position == "defender":
                    pos_scale = random.randint(40,70)/100
                else:
                    pos_scale = random.randint(60,100)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                attribute.level = round(random.randint(70,100) * age_scale * total_rating  * pos_scale)
            #Goalkeeper attributes
            if attribute.name == "Saveing":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(90,100)/100
                else:
                    pos_scale = random.randint(1,25)/100
                age_scale = (-0.2511 * self.age * self.age + 13.5 * self.age - 81.4481)/100
                base_skill = random.randint(90,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            if attribute.name == "Reflexes":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(80,100)/100
                else:
                    pos_scale = random.randint(1,25)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(90,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            if attribute.name == "Placement":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(80,100)/100
                else:
                    pos_scale = random.randint(1,25)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(90,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            if attribute.name == "Throwing":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(60,100)/100
                else:
                    pos_scale = random.randint(1,15)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(90,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            #Other player attributes
            if attribute.name == "Dribbling":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(1,40)/100
                elif self.position == "defender":
                    pos_scale = random.randint(45,70)/100
                elif self.position == "half back":
                    pos_scale = random.randint(60,90)/100
                elif self.position == "midfielder":
                    pos_scale = random.randint(60,100)/100
                else:
                    pos_scale = random.randint(70,100)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(80,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            if attribute.name == "Corners":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(1,40)/100
                elif self.position == "defender":
                    pos_scale = random.randint(45,70)/100
                elif self.position == "half back":
                    pos_scale = random.randint(60,90)/100
                elif self.position == "midfielder":
                    pos_scale = random.randint(60,100)/100
                else:
                    pos_scale = random.randint(70,100)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(80,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            if attribute.name == "Passing":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(1,40)/100
                elif self.position == "defender":
                    pos_scale = random.randint(45,70)/100
                elif self.position == "half back":
                    pos_scale = random.randint(60,90)/100
                elif self.position == "midfielder":
                    pos_scale = random.randint(60,100)/100
                else:
                    pos_scale = random.randint(70,100)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(80,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            if attribute.name == "Long pass":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(1,40)/100
                elif self.position == "defender":
                    pos_scale = random.randint(70,100)/100
                elif self.position == "half back":
                    pos_scale = random.randint(60,90)/100
                elif self.position == "midfielder":
                    pos_scale = random.randint(30,60)/100
                else:
                    pos_scale = random.randint(20,40)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(80,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            if attribute.name == "Shooting":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(1,40)/100
                elif self.position == "defender":
                    pos_scale = random.randint(45,70)/100
                elif self.position == "half back":
                    pos_scale = random.randint(60,90)/100
                elif self.position == "midfielder":
                    pos_scale = random.randint(60,100)/100
                else:
                    pos_scale = random.randint(70,100)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(80,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)
            if attribute.name == "Intercept":
                if self.position == "goalkeeper":
                    pos_scale = random.randint(1,40)/100
                elif self.position == "defender":
                    pos_scale = random.randint(70,100)/100
                elif self.position == "half back":
                    pos_scale = random.randint(60,90)/100
                elif self.position == "midfielder":
                    pos_scale = random.randint(50,80)/100
                else:
                    pos_scale = random.randint(30,60)/100
                age_scale = (-0.3125 * self.age * self.age + 16.25 * self.age - 111.25)/100
                base_skill = random.randint(80,100)
                attribute.level = round(base_skill * age_scale * total_rating * pos_scale)



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

    def calculate_composite_values(self, position):
        if position == 'goalkeeper':
            defense_stat = (0.5 * self.attributes[0].level + 0.25 * self.attributes[1].level + 0.2 * self.attributes[2].level + 0.05 * self.attributes[3].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            offense_stat = self.attributes[3].level * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            return (offense_stat, defense_stat)
        if position == 'libero':
            offense_stat = (0.1 * self.attributes[5].level + 0.1 * self.attributes[6].level + 0.15 * self.attributes[7].level + 0.30 * self.attributes[9].level + 0.05 * self.attributes[10].level + 0.10 * self.attributes[11].level + 0.05 * self.attributes[12].level + 0.10 * self.attributes[14].level + 0.05 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            defense_stat = (0.05 * self.attributes[7].level + 0.70 * self.attributes[8].level + 0.05 * self.attributes[9].level + 0.05 * self.attributes[11].level + 0.05 * self.attributes[12].level + 0.05 * self.attributes[13].level + 0.05 * self.attributes[14].level + 0.05 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            return (offense_stat, defense_stat)
        if position == 'leftdef' or position == 'rightdef':
            offense_stat = (0.1 * self.attributes[5].level + 0.1 * self.attributes[6].level + 0.15 * self.attributes[7].level + 0.30 * self.attributes[9].level + 0.05 * self.attributes[10].level + 0.10 * self.attributes[11].level + 0.05 * self.attributes[12].level + 0.10 * self.attributes[14].level + 0.05 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            defense_stat = (0.10 * self.attributes[7].level + 0.65 * self.attributes[8].level + 0.05 * self.attributes[9].level + 0.05 * self.attributes[11].level + 0.05 * self.attributes[12].level + 0.05 * self.attributes[13].level + 0.05 * self.attributes[14].level + 0.05 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            return (offense_stat, defense_stat)
        if position == 'lefthalf' or position == 'righthalf':
            offense_stat = (0.1 * self.attributes[5].level + 0.1 * self.attributes[6].level + 0.15 * self.attributes[7].level + 0.25 * self.attributes[9].level + 0.10 * self.attributes[10].level + 0.10 * self.attributes[11].level + 0.05 * self.attributes[12].level + 0.10 * self.attributes[14].level + 0.05 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            defense_stat = (0.05 * self.attributes[7].level + 0.60 * self.attributes[8].level + 0.05 * self.attributes[9].level + 0.10 * self.attributes[11].level + 0.05 * self.attributes[12].level + 0.10 * self.attributes[14].level + 0.05 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            return (offense_stat, defense_stat)
        if position == 'leftmid' or position == 'centralmid' or position == 'rightmid':
            offense_stat = (0.15 * self.attributes[5].level + 0.05 * self.attributes[6].level + 0.15 * self.attributes[7].level + 0.15 * self.attributes[9].level + 0.15 * self.attributes[10].level + 0.10 * self.attributes[11].level + 0.10 * self.attributes[12].level + 0.10 * self.attributes[14].level + 0.10 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            defense_stat = (0.05 * self.attributes[7].level + 0.40 * self.attributes[8].level + 0.05 * self.attributes[9].level + 0.20 * self.attributes[11].level + 0.10 * self.attributes[12].level + 0.10 * self.attributes[14].level + 0.10 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            return (offense_stat, defense_stat)
        if position == 'leftattack' or position == 'rightattack':
            offense_stat = (0.15 * self.attributes[5].level + 0.15 * self.attributes[7].level + 0.30 * self.attributes[10].level + 0.10 * self.attributes[11].level + 0.10 * self.attributes[12].level + 0.10 * self.attributes[14].level + 0.10 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            defense_stat = (0.35 * self.attributes[8].level + 0.35 * self.attributes[11].level + 0.10 * self.attributes[12].level + 0.10 * self.attributes[14].level + 0.10 * self.attributes[15].level) * (0.018 * self.attributes[15].level - 0.00008 * self.attributes[15].level ** 2)
            return (offense_stat, defense_stat)

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

