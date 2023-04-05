import json

class Club:
    def __init__(self, name, country, rating, home_arena):
        self.name = name
        self.country = country
        self.rating = rating
        self.home_arena = home_arena
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

class Team:
    def __init__(self, name, team_type):
        self.name = name
        self.team_type = team_type

def read_clubs_from_json(json_file):
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

clubs_data = read_clubs_from_json('data/clubs.json')
for club in clubs_data:
    print(club.name)
    for team in club.teams:
        print(f"- {team.name} ({team.team_type})")
