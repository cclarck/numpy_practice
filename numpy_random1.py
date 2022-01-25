#!/usr/bin/env python3
# 01.25.2022 10:17:44 CST
# title = numpy basic statistics
# description: generating random sample height, weight to do some calculate



import numpy as np

height = np.round(np.random.normal(1.74, 0.20, 5000), 2)
weight = np.round(np.random.normal(65, 15, 5000), 2)

print(f"Height data(unit: M): {height}")
print(f"Weight data(unit: KG): {weight}")

height_mean = np.mean(height)
weight_mean = np.mean(weight)

height_median = np.median(height)
weight_median = np.median(weight)

print(f"height (unit: M), mean: {height_mean}, median: {height_median}")
print(f"weight (unit: KG), mean: {weight_mean}, median: {weight_median}")
