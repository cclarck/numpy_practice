#!/usr/bin/env python3
# 01.24.2022 17:22:13 CST
# title = numpy test 3
# 2D numpy

import numpy as np
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)

print(type(np_baseball))

print(np_baseball.shape)
