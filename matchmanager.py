class MatchManager:
    def __init__(self):
        self.matches = []
    
    def add_match(self, match):
        self.matches.append(match)
    
    def get_all_matches(self):
        return self.matches
