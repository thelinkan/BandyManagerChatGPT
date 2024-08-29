from team import Team

class Manager:
    def __init__(self):
        self.name:str = ""
        self.age:int = 0
        self.team: int|Team = -1
        # self.gender = gender
        # self.skills = {}

    def train(self, skill):
        # improve a skill
        pass

    def set_name(self, name: str):
        self.name = name

    def set_age(self, age: int):
        self.age = age

    def set_team(self, team: Team):
        self.team = team

    def return_name(self) -> str:
        return self.name

    def return_age(self) -> int:
        return self.age

    def return_team(self) -> int|Team:
        return self.team

