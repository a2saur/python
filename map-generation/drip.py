import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

cWIDTH = 150
cHEIGHT = 150
cSEEDS = 5
cSHIFT = 1
cSINK = 1.5

def random_up_down(options, probability_sep):
  x = random.randrange(100)
  if x < probability_sep:
    return options[0]
  else:
    return options[1]

surrounding = [
               (-1, 1),(0, 1),(1, 1),
               (-1, 0),(1, 0),
               (-1,-1),(0,-1),(1,-1)
]
def spread(map, location, value):
  if location[0] < 0 or location[0] >= cWIDTH:
    return
  elif location[1] < 0 or location[1] >= cHEIGHT:
    return
  map[location[0], location[1]] = value
  for loc in surrounding:
    sur_loc = [location[0]+loc[0], location[1]+loc[1]]
    try:
      if map[sur_loc[0], sur_loc[1]] < value-cSHIFT and value-cSHIFT > 0:
        spread(map, sur_loc, value-random_up_down([-cSHIFT, cSHIFT], 4))
    except IndexError:
      pass

def sink(map, location, value, sunken):
  if sunken[location[0], location[1]] > value:
    return
  elif location[0] < 0 or location[0] >= cWIDTH:
    return
  elif location[1] < 0 or location[1] >= cHEIGHT:
    return
  sunken[location[0], location[1]] = value
  for loc in surrounding:
    sur_loc = [location[0]+loc[0], location[1]+loc[1]]
    try:
      if value-cSINK > 0:
        sink(map, sur_loc, value-cSINK, sunken)
    except IndexError:
      pass

# x, y
map = np.zeros((cWIDTH, cHEIGHT))
start_val = random.randrange(20, 40)
# print(start_val)
spread(map, (random.randrange(10, cWIDTH-10), random.randrange(10, cHEIGHT-10)), start_val)

sunken = np.zeros((cWIDTH, cHEIGHT))
sink_start_val = random.randrange(10, 20)
# print(sink_start_val)
sink(map, (random.randrange(10, cWIDTH-10), random.randrange(10, cHEIGHT-10)), sink_start_val, sunken)

for x in range(cWIDTH):
  for y in range(cHEIGHT):
    map[x, y] -= sunken[x, y]

to_plot = map.transpose()
plt.imshow(to_plot)
plt.gca().invert_yaxis()
plt.colorbar()
plt.show()
