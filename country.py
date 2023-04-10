import os
import json
import pygame
import random

class Country:
    def __init__(self, name, flag_path, bandy_knowledge, population, male_proficiency, female_proficiency):
        self.name = name
        self.flag_path = flag_path
        self.bandy_knowledge = bandy_knowledge
        self.population = population
        self.male_proficiency = male_proficiency
        self.female_proficiency = female_proficiency
        self.flag = pygame.image.load(self.flag_path).convert_alpha()
        self.flag_small = pygame.transform.scale(self.flag, (20, 20))
        self.load_names()

    def load_names(self):
        filename = "data/" + self.name.lower() + '_names.json'
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.male_first_names = data['male_first_names']
                self.female_first_names = data['female_first_names']
                self.family_names = data['family_names']
 
    def random_name(self,name_type):
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
 
    def to_dict(self):
        return {
            'name': self.name,
            'flag_path': self.flag_path,
            'population': self.population,
            'bandy_knowledge': self.bandy_knowledge,
            'male_proficiency': self.male_proficiency,
            'female_proficiency': self.female_proficiency
        }
        
    def return_flag(self):
        return self.flag_small
        
    def return_name(self):
        return self.name
