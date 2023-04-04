import json
from manager import Manager

class Game:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        #self.manager = Manager()
        #self.countries = []
        #self.leagues = []
        #self.clubs = []

    def load_game(self, file_path):
        with open('save_game.json', 'r') as file:
            game_data = json.load(file)
        self.year = game_data['year']
        self.month = game_data['month']
        self.day = game_data['day']
        # load game from file
        print(self.year)
        pass
    
    def new_game(self):
        # create new game
        pass

    def save_game(self, file_path):
        game_data = {
                'year': self.year,
                'month': self.month,
                'day': self.day
            }
        with open('save_game.json','w') as file:
            json.dump(game_data, file, indent=4)
        print("Game Data Saved")
        # save game to file
        pass
    
    def quit_game(self):
        # quit game
        pass
