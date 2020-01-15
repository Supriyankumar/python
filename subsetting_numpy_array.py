# height and weight are available as a regular lists
height_in = [4,4.5,6,5.5,5.4]
weight_lb = [70,85,72.5,90,80]
# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[3])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[1: 6])
