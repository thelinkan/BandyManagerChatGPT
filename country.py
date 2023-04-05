import pygame

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
