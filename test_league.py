# Import the League class from league.py
from league import League

# Create a League object with 4 teams
teams = ['Ljusdal', 'Edsbyn', 'Broberg', 'Bollnäs']
bandy_league = League(teams=teams, num_rounds=6, win_points=2, draw_points=1 )

# Print the league schedule
bandy_league.print_schedule()
