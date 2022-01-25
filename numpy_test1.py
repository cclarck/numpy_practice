#!/usr/bin/env python3
# 01.24.2022 14:28:34 CST
# title = numpy test 1
# description: BMI

import numpy as np

# Calculate the BMI
height_ft = [7.7, 7.6, 7.5, 7.4, 7.3, 7.2, 7.1]
weight_lb = [315, 200, 311, 302, 275, 217, 240]

np_height_in = np.array(height_ft) * 12
np_height_m = np_height_in * 0.0245
print(np_height_m)

np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
print(bmi)

# Create the light array
light = np.array(bmi < 25)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
