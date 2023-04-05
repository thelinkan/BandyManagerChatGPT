import json
from manager import Manager
from country import Country

class Game:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        self.manager = Manager()
        #self.countries = []
        #self.leagues = []
        #self.clubs = []

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
        self.countries = {}
        for country_data in countries_data:
            name = country_data['name']
            bandy_knowledge = country_data['bandy_knowledge']
            population = country_data['population']
            flag_path = country_data['flag_path']
            male_proficiency = country_data['male_proficiency']
            female_proficiency = country_data['female_proficiency']
            self.countries[name] = Country(name, flag_path, bandy_knowledge, population, male_proficiency, female_proficiency)
        #keys = self.countries.keys()
        #print(keys)
        #values = self.countries.values()
        #print(values)

    def save_game(self, file_path):
        countries_data = []
        for key, value in self.countries.items():
            countries_data.append(value.to_dict())
            
        game_data = {
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'manager_name': self.manager.return_name(),
                'manager_age': self.manager.return_age(),
                'countries': countries_data
            }
        with open('savedgames/save_game.json','w') as file:
            json.dump(game_data, file, indent=4)
        print("Game Data Saved")
        # save game to file
        pass
    
    def quit_game(self):
        # quit game
        pass
