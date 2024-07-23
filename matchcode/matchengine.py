import time
import random

class MatchEngine:
    def __init__(self, match):
        self.match = match
        self.time_scaling_factor = 20
        self.game_time = 0
        self.last_time = time.time()

    def tick(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        game_time_delta = elapsed_time * self.time_scaling_factor
        print(f"{game_time_delta=}")
        game_time_delta = 2

        #print(game_time_delta)
        self.game_time += game_time_delta
        self.last_time = current_time

        # Update game state based on the passage of time
        # This could include things like player movement, ball physics, etc.
        # You can define methods within the match class to handle these updates.
        self.match.update_state(manager=self, game_time_delta=game_time_delta)


    def get_current_time(self):
        seconds = int(self.game_time)
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

