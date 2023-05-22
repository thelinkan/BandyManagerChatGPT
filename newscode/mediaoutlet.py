class MediaOutlet:
    def __init__(self,name,type,country):
        self.name = name
        self.type = type
        self.country = country
        
    def to_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'country': self.country
        }
