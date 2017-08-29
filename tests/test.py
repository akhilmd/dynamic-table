#!/usr/bin/env python3

from matplotlib import pyplot as plt

import dynamic_table as dt

inc_factors = [1.25, 1.5, 1.75, 2, 3]


for inc_factor in inc_factors:
  print("Testing for inc_factor:", inc_factor)
  dt1 = dt.new(1, inc_factor, inc_factor, False)

  rts = [0]
  rt = 0

  for i in range(10):
    print(i)
    rt = dt.push(dt1, i)
    # dt.display(dt1)
    # print(rt, "\n")
    rts.append(rts[-1]+rt)

  for i in range(10):
    print(i)
    rt = dt.pop(dt1)
  dt.destroy(dt1)
  plt.plot(rts, label=str(inc_factor))
plt.legend(loc='upper left')
