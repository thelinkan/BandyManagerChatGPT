import random

# Define the initial schedule
schedule = [[(1,2),(3,4)],[(2,3),(4,1)],[(1,3),(2,4)]]

# Shuffle the order of the rounds
random.shuffle(schedule)

# Print the final schedule
print(schedule)
