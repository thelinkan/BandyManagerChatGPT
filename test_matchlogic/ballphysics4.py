import math

# Constants
GRAVITY = 9.81  # m/s^2
BALL_RADIUS = 0.062  # m
INITIAL_VELOCITY = 10  # m/s
ANGLE_DEGREES = 60  # degrees
COEFF_RESTITUTION = 0.3  # coefficient of restitution for bouncing

# Convert angle to radians
ANGLE_RADIANS = math.radians(ANGLE_DEGREES)

# Calculate initial velocity components
v_x = INITIAL_VELOCITY * math.cos(ANGLE_RADIANS)
v_y = INITIAL_VELOCITY * math.sin(ANGLE_RADIANS)

# Simulation parameters
time_step = 0.01  # s
total_time = 10  # s

# Initialize position and velocity
x = 0
y = BALL_RADIUS
vx = v_x
vy = v_y

# Simulation loop
while x < 50:  # Distance in meters to simulate
    # Calculate acceleration
    if y > BALL_RADIUS:
        ax = 0
        ay = -GRAVITY
    else:
        # Ball is on the ground
        ax = -vx * COEFF_RESTITUTION  # Ball slows down in x-direction due to friction with ground
        ay = 0

    # Update velocity
    vx += ax * time_step
    vy += ay * time_step

    # Update position
    x += vx * time_step
    y += vy * time_step

    # If ball hits the ground, bounce
    if y < BALL_RADIUS:
        y = BALL_RADIUS  # Set y-position to be exactly on the ground
        vy = -vy * COEFF_RESTITUTION  # Bounce with coefficient of restitution

    # Print ball position
    print(f"x: {x:.2f}, y: {y:.2f}, vx: {vx:.2f}, vy: {vy:.2f}")

    if vx < 0.1:
        break
