class Team:
    def __init__(self, name, country, is_male):
        self.name = name
        self.country = country
        self.is_male = is_male
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)