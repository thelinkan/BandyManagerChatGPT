import pickle

# Define your classes here
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

class Club:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams

# Create instances of your classes
player1 = Player("Kalle", 25)
player2 = Player("Alice", 28)
player3 = Player("Hans", 33)
team1 = Team("Team B", [player1, player2])
club1 = Club("Club 1", [team1])


# Serialize the entire class structure into a save file using pickle.dump()
#with open("save_game.pickle", "wb") as f:
#    pickle.dump(club1, f)

# Deserialize the entire class structure from the save file using pickle.load()
with open("save_game.pickle", "rb") as f:
    loaded_club = pickle.load(f)

# Access the deserialized objects and their attributes
print(loaded_club.name)                  # Output: Club 1
print(loaded_club.teams[0].name)         # Output: Team A
print(loaded_club.teams[0].players[0].name)  # Output: John
print(loaded_club.teams[0].players[1].name) 
