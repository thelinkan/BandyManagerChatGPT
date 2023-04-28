import math

# Constants
GRAVITY = 9.81  # m/s^2
BALL_RADIUS = 0.062  # m
INITIAL_VELOCITY = 20  # m/s
ANGLE_DEGREES = 88  # degrees

# Convert angle to radians
ANGLE_RADIANS = math.radians(ANGLE_DEGREES)

# Calculate initial velocity components
v_x = INITIAL_VELOCITY * math.cos(ANGLE_RADIANS)
v_y = INITIAL_VELOCITY * math.sin(ANGLE_RADIANS)

# Simulation parameters
time_step = 0.01  # s
total_time = 5  # s

# Initialize position and velocity
x = 0
y = BALL_RADIUS
vx = v_x
vy = v_y

# Simulation loop
while x < 50:  # Distance in meters to simulate
    # Calculate acceleration
    ax = 0
    ay = -GRAVITY

    # Update velocity
    vx += ax * time_step
    vy += ay * time_step

    # Update position
    x += vx * time_step
    y += vy * time_step

    # If ball hits the ground, stop simulation
    if y < BALL_RADIUS:
        break

    # Print ball position
    print(f"x: {x:.2f}, y: {y:.2f}")
