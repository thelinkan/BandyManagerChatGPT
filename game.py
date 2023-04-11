import json
import random
from manager import Manager
from country import Country
from club import Club
from team import Team
from person import Player
from person import PlayerManager
from uuidencoder import UUIDEncoder

class Game:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        self.manager = Manager()
        self.countries = {}
        #self.leagues = []
        self.clubs = []
        self.player_manager = PlayerManager()

    def new_game(self,manager_name,manager_age):
        # create new game
        # Set name and age
        self.manager.set_name(manager_name)
        self.manager.set_age(manager_age)
        with open('data/countries.json') as f:
            countries_data = json.load(f)
        #self.countries = {}
        for country_data in countries_data:
            name = country_data['name']
            bandy_knowledge = country_data['bandy_knowledge']
            population = country_data['population']
            flag_path = country_data['flag_path']
            male_proficiency = country_data['male_proficiency']
            female_proficiency = country_data['female_proficiency']
            self.countries[name] = Country(name, flag_path, bandy_knowledge, population, male_proficiency, female_proficiency)
        with open('data/clubs.json') as f:
            data = json.load(f)
        print(data)
        self.clubs = self.read_clubs_from_json(data)
        for club in self.clubs:
            print(club.name)
            for team in club.teams:
                if (team.team_type == "Men" or team.team_type == "Men U19"):
                    gender="male"
                else:
                    gender="female"
                player_first_name = ""
                player_familyname = ""
                antspelare = team.num_players
                print(f"- {team.name} ({team.team_type})")
                for i in range(antspelare):
                    for key, value in self.countries.items():
                        if(key == club.country):
                            if(gender == "male"):
                                player_first_name = value.random_name("male")
                            else:
                                player_first_name = value.random_name("female")
                            player_familyname = value.random_name("family")
                        #print(f"== {key} == {value} ==")
                    age = random.randint(20,36)
                    #team.create_player(player_first_name,player_familyname,age,gender,"forward",team)
                    if (i == 0 or i == 14):
                        position = "goalkeeper"
                    elif (i>=1 and i<=4):
                        position = "defender"
                    elif (i>=5 and i<=7):
                        position = "half back"
                    elif ((i>=8 and i<=11) or (i>=15 and i<=16)):
                        position = "midfielder"
                    elif ((i>=12 and i<=13) or (i>=17 and i<=18)):
                        position = "forward"
                    player = self.player_manager.create_player(player_first_name, player_familyname, age, gender, position, team)
                    team.add_player(player)
                    print(f"- - {player.__str__()}")
                team.print_players()
        #print(self.countries['Sweden'].male_first_names)
        #keys = self.countries.keys()
        #print(keys)
        #values = self.countries.values()
        #print(values)

    def load_game(self, file_path):
        # load game from file
        with open('savedgames/save_game.json', 'r') as file:
            game_data = json.load(file)
        self.year = game_data['year']
        self.month = game_data['month']
        self.day = game_data['day']
        manager_data = game_data['manager']
        self.manager.set_name(manager_data['name'])
        self.manager.set_age(manager_data['age'])
        self.manager.set_team(manager_data['team'])
        self.countries = {}
        for country_data in game_data['countries']:
            name = country_data['name']
            bandy_knowledge = country_data['bandy_knowledge']
            population = country_data['population']
            flag_path = country_data['flag_path']
            male_proficiency = country_data['male_proficiency']
            female_proficiency = country_data['female_proficiency']
            self.countries[name] = Country(name, flag_path, bandy_knowledge, population, male_proficiency, female_proficiency)
        #print(game_data['club_data'])
        players_data = game_data.get('players_data', [])
        for player_load in players_data:
            print(player_load)
        #print(game_data['players_data'])
        #PlayerManager.from_list(self, game_data['players_data'])
        #self.player_manager.from_list(game_data['players_data'])


        self.clubs = self.read_clubs_from_json(game_data['club_data'])
        for club in self.clubs:
            print(club.name)
            for team in club.teams:
                print(f"- {team.name} ({team.team_type})")

        #for key, value in self.countries.items():
        #    print(value.to_dict())
        print("Data loaded")
        #print(self.year)
        #print(self.manager.return_team())

    def save_game(self, file_path):
        # save game to file
        countries_data = []
        clubs_data =[]
        players = []
        player_data = []

        for key, value in self.countries.items():
            countries_data.append(value.to_dict())
        for club in self.clubs:
            clubs_data.append(club.to_dict())
            for team in club.teams:
                print(f"save: {team.name}");
                for player in team.players:
                    if player not in players:
                         players.append(player)

        players_data = [player.to_dict() for player in players]

        game_data = {
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'manager': {
                    'name': self.manager.return_name(),
                    'age': self.manager.return_age(),
                    'team': self.manager.return_team()
                },
                'countries': countries_data,
                'club_data':{
                    'clubs': clubs_data
                },
                'players_data': players_data
            }
        with open('savedgames/save_game.json','w') as file:
            json.dump(game_data, file, indent=4, cls=UUIDEncoder)
        print("Game Data Saved")

    def set_manager_team(self,team):
        self.manager.set_team(team)

    def return_manager_team(self):
        self.manager.return_team

    def return_managername(self):
        return self.manager.return_name()

    def return_countrylist(self):
        countries_list = list(self.countries.values())
        countries_list.sort(key=lambda country: country.name)
        return countries_list

    def return_countryflag(self,country_name):
         for country in self.countries.values():
            if country.name == country_name:
                return country.return_flag()

    def read_clubs_from_json(self,data):

        clubs = []

        for club_data in data['clubs']:
            name = club_data['name']
            country = club_data['country']
            rating = club_data['club_rating']
            home_arena = club_data['home_arena']
            club = Club(name, country, rating, home_arena)

            for team_data in club_data['teams']:
                name = team_data['name']
                team_type = team_data['team_type']
                team_rating = team_data['team_rating']
                num_players = team_data['num_players']
                num_int_players = team_data['num_int_players']
                team = Team(name, team_type, team_rating, num_players, num_int_players)
                club.add_team(team)

            clubs.append(club)

        return clubs

    def return_teamlist(self, country, teamtype):
        team_list = []
        for club in self.clubs:
            if club.country == country:
                teams = club.get_teams_by_type(teamtype)
                team_list.extend(teams)
        return team_list

    def tick(self):
        self.day += 1
        if self.month in [4, 6, 9, 11]:
            month_days = 30
        elif self.month == 2:
            if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
                month_days = 29
            else:
                month_days = 28
        else:
            month_days = 31

        if self.day > month_days:
            self.day = 1
            self.month += 1

        if self.month > 12:
            self.month = 1
            self.year += 1

    def quit_game(self):
        # quit game
        pass
