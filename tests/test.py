#!/usr/bin/env python3

from matplotlib import pyplot as plt
import sys
from random import randint

import dynamic_table as dt

factors = [1.25, 1.5, 1.75, 2, 3]

fig_i, ax_i = plt.subplots( nrows=1, ncols=1 )
fig_d, ax_d = plt.subplots( nrows=1, ncols=1 )

n = int(sys.argv[1])

# Test for All inserts before deletes.
for inc_factor in factors:
  print("Testing all inserts before deletes for factor:", inc_factor)

  # Create new DynamicTable with initial size 1,
  # same inc_factor and dec_factor and to use malloc+memcpy 
  # as ooposed to realloc while allocating more memory.
  dt1 = dt.new(1, inc_factor, inc_factor, True)

  rts = [0]
  rt = 0
  mxi = 0
  mx = 0

  # Push n times and check which insertion took the longest.
  for i in range(n):
    rt = dt.push(dt1, i)
    if rt > mx:
      mxi = i
      mx = rt
    # Add to previous to get a cumulative plot.
    rts.append(rts[-1]+rt)

  # Plot the values.
  p = ax_i.plot(rts, label=str(inc_factor), linewidth=2)

  # Draw arrow for the max.
  ax_i.annotate(
    str(inc_factor),
    xy = (mxi, rts[mxi+1]+0.5),
    xytext = (mxi + 15, rts[mxi]+10),
    arrowprops = dict(facecolor=p[0].get_color(), shrink=0.005)
  )

  rts = [0]
  mxi = 0
  mx = 0

  # Pop n times and check which deletion took the longest
  # since this operation is guaranteed to be constant time,
  # this plot should not contain anything interesting.
  for i in range(n):
    rt = dt.pop(dt1)
    if rt > mx:
      mxi = i
      mx = rt
    rts.append(rts[-1]+rt)
  
  # Plot the run times.
  p = ax_d.plot(rts, label=str(inc_factor), linewidth=2)

  # Draw arrow for the max.
  ax_d.annotate(
    str(inc_factor),
    xy = (mxi, rts[mxi+1]+0.5),
    xytext = (mxi + 15, rts[mxi]+10),
    arrowprops = dict(facecolor=p[0].get_color(), shrink=0.005)
  )

  # Free all memory to prevent leaks.
  dt.destroy(dt1)

# plots for push and pop graphs.
ax_i.legend(loc='upper left')
ax_i.set_xlabel("Number of insertions")
ax_i.set_ylabel("Time from first insertion")
# fig_i.savefig("ins.png")

ax_d.legend(loc='upper left')
ax_d.set_xlabel("Number of deletion")
ax_d.set_ylabel("Time from first deletion")
# fig_d.savefig("del.png")

# Test for random sequence of operations with
# various ratios.
ratios = [3/2, 4/2]

for ratio in ratios:
  print("\n\nPopulating operations with ratio:", ratio)

  # calculate no. of pops and pushes.
  pops = int(n/(1+ratio))
  pushs = n - pops
  allowedPopCount = 0

  # A data structure to hold sequence of operations.
  # 1 is push, 0 is pop
  ops = []

  # This is required to guarantee randomness and also
  # to maintain that there must be enough elements inserted
  # to delete them
  for i in range(pushs + pops):
    if allowedPopCount > 0:
      if pushs > 0 and pops >0:
        k = randint(0,1)
        if k == 1:
          ops.append(1)
          pushs -= 1
          allowedPopCount += 1
        else:
          ops.append(0)
          pops -= 1
          allowedPopCount -= 1
      elif pops > 0:
        ops.append(0)
        pops -= 1
        allowedPopCount -= 1
      elif pushs > 0:
        ops.append(1)
        pushs -= 1
        allowedPopCount += 1
    else:
      ops.append(1)
      pushs -= 1
      allowedPopCount += 1

  # to hold most of the captured data.
  #   mxi: maximum time for insertion
  #   mxd: maximum time for deletion
  #   avgop: average time for operation
  #   avgi: avergae time for insertions
  #   avgd: average time for deletions
  table = {
    factor: {
      factor: {
        "mxi": 0,
        "mxd": 0,
        "avgop": 0,
        "avgi": 0,
        "avgd": 0
      } for factor in factors} for factor in factors}

  # get statistics for each combination of factors
  # for the above generated operations.
  for inc_factor in factors:
    for dec_factor in factors:
      pair = (inc_factor, dec_factor)
      print("Operating with factors: ", pair)

      # Create new Data Structure
      dt1 = dt.new(1, pair[0], pair[1], True)

      insertions = 0
      deletions = 0

      # Apply operations and capture time and statistics
      for op in ops:
        runTime = 0
        if op == 1:
          runTime = dt.push(dt1, randint(0, 99999))

          if runTime > table[pair[0]][pair[1]]["mxi"]:
            table[pair[0]][pair[1]]["mxi"] = runTime

          table[pair[0]][pair[1]]["avgi"] =  (table[pair[0]][pair[1]]["avgi"] * insertions + runTime) / (insertions+1)
          insertions += 1
        elif op == 0:
          runTime = dt.pop(dt1)

          if runTime > table[pair[0]][pair[1]]["mxd"]:
            table[pair[0]][pair[1]]["mxd"] = runTime

          table[pair[0]][pair[1]]["avgd"] =  (table[pair[0]][pair[1]]["avgd"] * deletions + runTime) / (deletions+1)
          deletions += 1

        t = insertions + deletions
        table[pair[0]][pair[1]]["avgop"] = (table[pair[0]][pair[1]]["avgop"] * (t-1) + runTime) / t

      # Free memory to prevent leaks
      dt.destroy(dt1)

  stats = ["mxi", "mxd", "avgop", "avgi", "avgd"]

  print("\nAll times in milliseconds")

  # Print stats
  for stat in stats:
    print("statistic:",stat, "\tratio:", ratio)
    for inc_factor in factors:
      for dec_factor in factors:
        print("%.6f"%table[inc_factor][dec_factor][stat], end=" | ")
      print()
    print()

# display the plots.
plt.show()