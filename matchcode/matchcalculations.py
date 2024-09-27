import math

def calculate_distance_between_players(player1_position, player2_position):
    """
    Calculates the distance between two players on the field.
    
    :param player1_position: A tuple (x, y) representing the position of the first player.
    :param player2_position: A tuple (x, y) representing the position of the second player.
    
    :return: The distance between the two players.
    """
    x1, y1 = player1_position
    x2, y2 = player2_position
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def calculate_speed_for_tick(last_speed, chosen_acceleration, max_speed):
    """
    Calculates the speed for the current tick, ensuring it's within valid bounds.

    :param last_speed: The speed of the player in the previous tick (m/s).
    :param chosen_acceleration: The acceleration applied during this tick (m/s²).
    :param max_speed: The maximum speed of the player (m/s).
    :return: The updated speed for the current tick.
    """
    new_speed = last_speed + chosen_acceleration
    new_speed = max(0, min(max_speed, new_speed))
    
    return new_speed

def calculate_shortest_distance(ball_position, ball_vector, player_position):
    """
    Calculate the shortest distance from the player's position to the finite line segment
    defined by the ball's position and movement vector.

    :param ball_position: A tuple representing the ball's current position (x, y).
    :param ball_vector: A tuple representing the ball's movement vector (vx, vy).
    :param player_position: A tuple representing the player's current position (px, py).
    :return: The shortest distance from the player to the line segment.
    """
    # Ball position and movement vector
    bx, by = ball_position
    vx, vy = ball_vector
    
    # Player's position
    px, py = player_position
    
    # The endpoint of the ball's movement vector
    ex, ey = bx + vx, by + vy
    
    # Calculate the vector from the ball's position to the player's position
    ball_to_player = (px - bx, py - by)
    
    # Calculate the magnitude of the ball's movement vector
    ball_vector_magnitude = math.sqrt(vx**2 + vy**2)
    
    # Avoid division by zero in case the ball is not moving
    if ball_vector_magnitude == 0:
        return math.sqrt((px - bx)**2 + (py - by)**2)
    
    # Normalize the ball's movement vector
    ball_vector_normalized = (vx / ball_vector_magnitude, vy / ball_vector_magnitude)
    
    # Project the ball-to-player vector onto the ball's movement vector
    projection_length = (ball_to_player[0] * ball_vector_normalized[0] +
                         ball_to_player[1] * ball_vector_normalized[1])
    
    # Clamp the projection length to the range [0, ball_vector_magnitude] to stay within the segment
    projection_length_clamped = max(0, min(projection_length, ball_vector_magnitude))
    
    # Calculate the projection vector
    projection_vector = (projection_length_clamped * ball_vector_normalized[0],
                         projection_length_clamped * ball_vector_normalized[1])
    
    # Calculate the perpendicular (shortest) vector
    perpendicular_vector = (ball_to_player[0] - projection_vector[0],
                            ball_to_player[1] - projection_vector[1])
    
    # Calculate the magnitude of the perpendicular vector, which is the shortest distance
    shortest_distance = math.sqrt(perpendicular_vector[0]**2 + perpendicular_vector[1]**2)
    
    return shortest_distance

def calculate_direction(current_position: tuple,target_position:tuple) -> tuple:
    desired_direction =(
            target_position[0]-current_position[0],
            target_position[1]-current_position[1]
        )
    return desired_direction    

def calculate_angle(vec1, vec2):
    """Calculates the angle between two vectors."""
    dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    magnitude_vec1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
    magnitude_vec2 = math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)
    magnitude_multi = magnitude_vec1 * magnitude_vec2
    if magnitude_vec1 * magnitude_vec2 == 0:
        return 0
    if dot_product/magnitude_multi >= 1 or dot_product/magnitude_multi <= -1:
        return 0      
    return math.acos(dot_product / (magnitude_multi))

def calculate_max_turn_angle(last_vector):
    """
    Determines the maximum angle by which a player can turn 
    based on their speed.
    """
    # Calculate the magnitude (speed) of the last vector
    speed = math.sqrt(last_vector[0]**2 + last_vector[1]**2)        
    # Simple example: The faster the player, the smaller the max turn angle
    # This value can be fine-tuned based on how you want players to behave.
    return max(10, 90 - speed * 2)  # Just an example

def interpolate_direction(vec1, vec2, max_angle):
    """Interpolates between two directions by a limited angle."""
    angle_between = calculate_angle(vec1, vec2)
    ratio = min(1, max_angle / angle_between)
    return (
        vec1[0] * (1 - ratio) + vec2[0] * ratio,
        vec1[1] * (1 - ratio) + vec2[1] * ratio
    )

