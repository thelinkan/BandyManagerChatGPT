class Club:
    def __init__(self, name, country, rating, home_arena):
        self.name = name
        self.country = country
        self.rating = rating
        self.home_arena = home_arena
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def get_teams(self):
        return self.teams

class Team:
    def __init__(self, name, gender, club):
        self.name = name
        self.gender = gender
        self.club = club

club1 = Club("Sandvikens AIK", "Sweden", 90, "Jernvallen")
club2 = Club("AIK", "Sweden", 85, "Hovet")

team1 = Team("Sandvikens AIK", "Male", club1)
team2 = Team("Sandvikens AIK U19", "Male U19", club1)
team3 = Team("Sandvikens AIK", "Female", club1)
team4 = Team("Sandvikens AIK U19", "Female U19", club1)

team5 = Team("AIK", "Female", club2)
team6 = Team("AIK U19", "Female U19", club2)

club1.add_team(team1)
club1.add_team(team2)
club1.add_team(team3)
club1.add_team(team4)

club2.add_team(team5)
club2.add_team(team6)

for club in [club1, club2]:
    print("Club:", club.name)
    teams = club.get_teams()
    for team in teams:
        print(" -", team.name, "(" + team.gender + ")")
