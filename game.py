import json
from manager import Manager
from country import Country
from club import Club
from team import Team

class Game:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        self.manager = Manager()
        self.countries = {}
        #self.leagues = []
        self.clubs = []

    def load_game(self, file_path):
        # load game from file
        with open('savedgames/save_game.json', 'r') as file:
            game_data = json.load(file)
        self.year = game_data['year']
        self.month = game_data['month']
        self.day = game_data['day']
        self.manager.set_name(game_data['manager_name'])
        self.manager.set_age(game_data['manager_age'])
        self.countries = {}
        for country_data in game_data['countries']:
            name = country_data['name']
            bandy_knowledge = country_data['bandy_knowledge']
            population = country_data['population']
            flag_path = country_data['flag_path']
            male_proficiency = country_data['male_proficiency']
            female_proficiency = country_data['female_proficiency']
            self.countries[name] = Country(name, flag_path, bandy_knowledge, population, male_proficiency, female_proficiency)
        #for key, value in self.countries.items():
        #    print(value.to_dict())
        print("Data loaded")
        #print(self.year)
        #print(self.manager.return_age())

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
        self.clubs = self.read_clubs_from_json('data/clubs.json')
        for club in self.clubs:
            print(club.name)
            for team in club.teams:
                print(f"- {team.name} ({team.team_type})")

        #keys = self.countries.keys()
        #print(keys)
        #values = self.countries.values()
        #print(values)

    def save_game(self, file_path):
        countries_data = []
        clubs_data =[]
        for key, value in self.countries.items():
            countries_data.append(value.to_dict())
        for club in self.clubs:
            clubs_data.append(club.to_dict())

        game_data = {
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'manager_name': self.manager.return_name(),
                'manager_age': self.manager.return_age(),
                'countries': countries_data,
                'teams': clubs_data
            }
        with open('savedgames/save_game.json','w') as file:
            json.dump(game_data, file, indent=4)
        print("Game Data Saved")
        # save game to file

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

    def read_clubs_from_json(self,json_file):
        with open(json_file) as f:
            data = json.load(f)

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
                team = Team(name, team_type)
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



    def quit_game(self):
        # quit game
        pass
