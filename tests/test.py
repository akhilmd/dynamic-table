#!/usr/bin/env python3

from matplotlib import pyplot as plt

import dynamic_table as dt

dt1 = dt.new(2,1.5,1.5,True)

rt = 0

dt.display(dt1)

rt = dt.push(dt1, 100)
print("insertion took", rt, "ms")
dt.display(dt1)

rt = dt.push(dt1, 200)
print("insertion took", rt, "ms")
dt.display(dt1)

