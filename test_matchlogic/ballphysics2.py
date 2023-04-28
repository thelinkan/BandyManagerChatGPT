import math

# Constants
GRAVITY = 9.81  # m/s^2
BALL_RADIUS = 0.062  # m
INITIAL_VELOCITY = 20  # m/s
ANGLE_DEGREES_XZ = 40  # degrees
ANGLE_DEGREES_Y = 40  # degrees

# Convert angles to radians
ANGLE_RADIANS_XZ = math.radians(ANGLE_DEGREES_XZ)
ANGLE_RADIANS_Y = math.radians(ANGLE_DEGREES_Y)

# Calculate initial velocity components
v_x = INITIAL_VELOCITY * math.cos(ANGLE_RADIANS_Y) * math.cos(ANGLE_RADIANS_XZ)
v_y = INITIAL_VELOCITY * math.sin(ANGLE_RADIANS_Y)
v_z = INITIAL_VELOCITY * math.cos(ANGLE_RADIANS_Y) * math.sin(ANGLE_RADIANS_XZ)

# Simulation parameters
time_step = 0.01  # s
total_time = 5  # s

# Initialize position and velocity
x = 0
y = BALL_RADIUS
z = 0
vx = v_x
vy = v_y
vz = v_z

# Simulation loop
while y >= BALL_RADIUS:  # Stop when ball hits the ground
    # Calculate acceleration
    ax = 0
    ay = -GRAVITY
    az = 0

    # Update velocity
    vx += ax * time_step
    vy += ay * time_step
    vz += az * time_step

    # Update position
    x += vx * time_step
    y += vy * time_step
    z += vz * time_step

    # Print ball position
    print(f"x: {x:.2f}, y: {y:.2f}, z: {z:.2f}")
