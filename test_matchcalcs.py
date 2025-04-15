from matchcode.matchcalculations import calculate_shortest_distance

current_position = (30,40)
ball_position = (30,100)
ball_vector = (0,-5)

print(calculate_shortest_distance(ball_position, ball_vector, current_position))