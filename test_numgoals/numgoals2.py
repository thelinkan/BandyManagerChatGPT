import random
import numpy as np

def generate_value(input_value):
    # Scale lambda based on input value
    lambda_value = 5 * input_value

    # Generate a random value using the Poisson distribution
    value = np.random.poisson(lambda_value)

    # Ensure the value is non-negative
    value = max(value, 0)

    return value

print (generate_value(1))
