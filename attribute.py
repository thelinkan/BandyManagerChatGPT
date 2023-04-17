class Attribute:
    def __init__(self, name, level, experience):
        self.name = name
        self.level = level
        self.experience = experience

    def to_dict(self):
        return {
            'name': self.name,
            'level': self.level,
            'experience': self.experience
        }