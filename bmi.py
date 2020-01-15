import numpy as np

height = [1.1,2.3,4,5]
weight = [70,45,30,20.45]

# converting a list to numpy array

np_height_in = np.array(height)
print((np_height_in))

np_weight_in = np.array(weight)
print((np_weight_in))

# converting numpy array to m
np_height_m = np_height_in * 0.0254
print(np_height_m)

np_weight_m = np_weight_in * 0.453592
print(np_weight_m)

bmi = np_height_m / np_weight_m ** 2

print(bmi)