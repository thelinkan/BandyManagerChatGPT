class Attribute:
    '''
    Class of attributes for the players
    '''
    def __init__(self, name: str, level: int, experience: int):
        self.name: str = name
        self.level: int = level
        self.experience: int = experience

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'level': self.level,
            'experience': self.experience
        }