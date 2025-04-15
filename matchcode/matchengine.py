import time
import random

class MatchEngine:
    def __init__(self, match) -> None:
        self.match = match
        self.game_time = 0

    def tick(self, game) -> None:
        game_time_delta = 1
        self.game_time += game_time_delta

        # Update game state based on the passage of time
        # This could include things like player movement, ball physics, etc.
        # You can define methods within the match class to handle these updates.
        self.match.update_state(game, manager=self, game_time_delta=game_time_delta)


    def get_current_time(self) -> str:
        seconds = int(self.game_time)
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

