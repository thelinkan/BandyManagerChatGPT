def determine_field_area(home_away, position):
    """
    Determines which area of the field a given (x, y) coordinate belongs to.
    
    Coordinates go from (0,0) to (60,100).
    """

    x = position[0]
    y = position[1]
    # Define the field dimensions
    field_width = 60
    field_length = 100

    #if home_away == "away":
    #    y = field_length - y  # Flip the y-coordinate to mirror the field vertically
        
    # Goal Area (Rectangular)
    goal_area_width = 12  # 6m on each side from the center
    goal_area_length = 6   # 6m from the goal line
    if (field_width//2 - goal_area_width//2) <= x <= (field_width//2 + goal_area_width//2) and y <= goal_area_length:
        return "goal area"

    # Penalty Area (Semi-Circular and Rectangular)
    penalty_area_width = 32  # 16m on each side from the center
    penalty_area_length = 16  # 16m from the goal line
    penalty_radius = 16

    if (field_width//2 - penalty_area_width//2) <= x <= (field_width//2 + penalty_area_width//2) and y <= penalty_area_length:
        return "penalty area"
    
    # Check if within the penalty arc (outside the rectangle but within the radius)
    penalty_center_x = field_width // 2
    penalty_center_y = penalty_area_length
    distance_from_penalty_center = ((x - penalty_center_x) ** 2 + (y - penalty_center_y) ** 2) ** 0.5
    if distance_from_penalty_center <= penalty_radius:
        return "penalty area"
    
    # D-Zone (Arc)
    d_zone_radius = 9
    d_zone_center_y = penalty_area_length  # Same y-coordinate as the penalty center
    if distance_from_penalty_center <= d_zone_radius:
        return "D-zone"
    
    # Corner Areas (Triangular)
    corner_length = 5  # Arbitrary length from the corner flag
    if (x <= corner_length and y >= (field_length - corner_length)) or (x >= (field_width - corner_length) and y >= (field_length - corner_length)):
        return "corner area"

    # Wings (Rectangular)
    wing_width = 8
    if (x <= wing_width or x >= field_width - wing_width):
        return "wing"
    
    # Attacking Third (Rectangular)
    attacking_third_length = 33  # Length of attacking third
    if y > field_length - attacking_third_length:
        return "attacking third"
    
    # Defensive Third (Rectangular)
    defensive_third_length = 33  # Length of defensive third
    if y < defensive_third_length:
        return "defensive third"
    
    # Central Midfield (Rectangular)
    midfield_start = defensive_third_length
    midfield_end = field_length - attacking_third_length
    if midfield_start <= y <= midfield_end:
        return "central midfield"
    
    # Half-space (Rectangular)
    half_space_width = 10
    if (half_space_width < x < (field_width - half_space_width) and (y > defensive_third_length and y < field_length - attacking_third_length)):
        return "half-space"
    
    # Neutral Zone (Circle)
    center_circle_radius = 9
    center_x = field_width // 2
    center_y = field_length // 2
    distance_from_center = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
    if distance_from_center <= center_circle_radius:
        return "neutral zone"
    
    # If no other area matched, return "unknown area"
    return "unknown area"

def get_players_in_zones(team_positions, home_away, zones):
    """
    Returns a list of player positions for players in the specified zones.
    
    Parameters:
    - team_positions: Dictionary containing player positions (e.g., self.home_team_positions or self.away_team_positions).
    - home_away: 'home' or 'away', indicating which team's players to check.
    - zones: List of zones to check (e.g., ["goal area", "penalty area"]).
    
    Returns:
    - List of player positions for players found in the specified zones.
    """
    players_in_zones = []
    
    for player_position, position in team_positions.items():
        # Get the (x, y) position of the player
        x, y = position[:2]  # Ignore any z-coordinate or direction
        
        # Determine the area where this player is located
        player_zone = determine_field_area(home_away, (x, y))
        
        # Check if the player's zone is in the list of zones
        if player_zone in zones:
            players_in_zones.append(player_position)
    
    return players_in_zones

if __name__ == '__main__':
    print(determine_field_area("home",(3,97)))