import os
import json
import pygame
import random

class Country:
    def __init__(self, name: str, flag_path: str, bandy_knowledge: int, population: int, male_proficiency: int, female_proficiency: int):
        self.name = name
        self.flag_path = flag_path
        self.bandy_knowledge = bandy_knowledge
        self.population = population
        self.male_proficiency = male_proficiency
        self.female_proficiency = female_proficiency
        self.flag: pygame.Surface  = pygame.image.load(self.flag_path).convert_alpha()
        self.flag_small = pygame.transform.scale(self.flag, (20, 20))
        self.load_names()

    def load_names(self) -> None:
        filename = "data/names/" + self.name.lower() + '_names.json'
        #print (self.name.lower())
        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.male_first_names = data['male_first_names']
                self.female_first_names = data['female_first_names']
                self.family_names = data['family_names']

    def random_name(self,name_type: str) -> str:
        if(name_type == "male"):
            antnamn = len(self.male_first_names)
            randnamn = random.randint(0,antnamn-1)
            return(self.male_first_names[randnamn])
        if(name_type == "female"):
            antnamn = len(self.female_first_names)
            randnamn = random.randint(0,antnamn-1)
            return(self.female_first_names[randnamn])
        if(name_type == "family"):
            antnamn = len(self.family_names)
            randnamn = random.randint(0,antnamn-1)
            return(self.family_names[randnamn])
        return ""

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'flag_path': self.flag_path,
            'population': self.population,
            'bandy_knowledge': self.bandy_knowledge,
            'male_proficiency': self.male_proficiency,
            'female_proficiency': self.female_proficiency
        }

    def return_flag(self) -> pygame.Surface:
        return self.flag_small

    def return_name(self) -> str:
        return self.name
