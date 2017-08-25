#!/usr/bin/env python3

from matplotlib import pyplot as plt

import dynamic_table as dt

inc_factors = [1.25, 1.5, 1.75, 2, 3]


for inc_factor in inc_factors:
  print("Testing for inc_factor:", inc_factor)
  dt1 = dt.new(1, inc_factor, 1.5, False)

  rts = [0]
  rt = 0

  for i in range(1000000):
    rt = dt.push(dt1, i)
    # dt.display(dt1)
    # print(rt, "\n")
    rts.append(rts[-1]+rt)

  plt.plot(rts, label=str(inc_factor))
plt.legend(loc='upper left')
plt.show()
