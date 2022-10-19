import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

cWIDTH = 150
cHEIGHT = 150
cSEEDS = 5
cSHIFT = 1
cNUM_CONTINENTS = 5

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

group = [
               (-1, 1),(0, 1),(1, 1),
               (-1, 0),(0, 0),(1, 0),
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

def spread_value(map, location, value, empty_val="", r=0):
    if location[0] < 0 or location[0] >= cWIDTH:
        return
    elif location[1] < 0 or location[1] >= cHEIGHT:
        return
    elif map[location[0], location[1]] != empty_val:
        return
    elif r > 50:
        return
    map[location[0], location[1]] = value
    for loc in surrounding:
        sur_loc = [location[0]+loc[0], location[1]+loc[1]]
        try:
            spread_value(map, sur_loc, value, empty_val, r+1)
        except IndexError:
            pass

def contains(map, value):
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            if map[x, y] == value:
                return True
    return False

def direction_merge(dir1, dir2):
    if (dir1 == "U" and dir2 == "D") or (dir2 == "U" and dir1 == "D") or (dir1 == "R" and dir2 == "L") or (dir2 == "R" and dir1 == "L"):
        return ""
    elif dir1 == dir2:
        return dir1
    elif dir1 == "":
        return dir2
    elif dir2 == "":
        return dir1
    else:
        # return dir1+dir2
        return random.choice([dir1, dir2])

def blur(map):
    new_map = np.zeros((cWIDTH, cHEIGHT))
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            total = 0
            count = 0
            for loc in group:
                try:
                    total += map[x+loc[0], y+loc[1]]
                    count += 1
                except IndexError:
                    pass
            new_map[x, y] = int(total/count)
    return new_map

# x, y
map = np.zeros((cWIDTH, cHEIGHT))
for x in range(cWIDTH):
    for y in range(cHEIGHT):
        map[x, y] = 10
start_val = random.randrange(20, 40)
spread(map, (random.randrange(10, cWIDTH-10), random.randrange(10, cHEIGHT-10)), start_val)
spread(map, (random.randrange(10, cWIDTH-10), random.randrange(10, cHEIGHT-10)), start_val)
spread(map, (random.randrange(10, cWIDTH-10), random.randrange(10, cHEIGHT-10)), start_val)

dir_map = np.zeros((cWIDTH, cHEIGHT), dtype=str)
# for x in range(cNUM_CONTINENTS):
l = 0
while contains(dir_map, "") and l < 1000:
    position = [random.randrange(10, cWIDTH-10), random.randrange(10, cHEIGHT-10)]
    while map[position[0], position[1]] == "":
        position = [random.randrange(10, cWIDTH-10), random.randrange(10, cHEIGHT-10)]
    spread_value(dir_map, position, random.choice(list("UDLR")))
    l += 1


to_plot = map.transpose()
plt.imshow(to_plot)
plt.gca().invert_yaxis()
plt.colorbar()
plt.show()


# dir_map_color = np.zeros((cWIDTH, cHEIGHT))
# dir_colors = {
#     "U":1,
#     "D":2,
#     "L":3,
#     "R":4,
#     "":0
# }
# for x in range(cWIDTH):
#     for y in range(cHEIGHT):
#         dir_map_color[x, y] = dir_colors[dir_map[x, y]]

# to_plot = dir_map_color.transpose()
# plt.imshow(to_plot)
# plt.gca().invert_yaxis()
# plt.colorbar()
# plt.show()

for z in range(100):
    new_map = np.zeros((cWIDTH, cHEIGHT))
    new_dir = np.zeros((cWIDTH, cHEIGHT), dtype=str)
    for x in range(cWIDTH):
        for y in range(cHEIGHT):
            if True:#random.choice([0]*int(map[x, y])+[1]*500) == 1:
                try:
                    if "U" in dir_map[x, y]:
                        # if new_map[x, y+1] == 0:
                        #     new_map[x, y+1] += map[x, y]
                        #     new_dir[x, y+1] = dir_map[x, y]
                        # else:
                        #     new_map[x, y+1] = max(new_map[x, y+1], map[x, y])+(min(new_map[x, y+1], map[x, y])*0.5)
                        #     new_dir[x, y+1] = direction_merge(new_dir[x, y+1], dir_map[x, y])
                        new_map[x, y+3] += map[x, y]
                        new_dir[x, y+3] = dir_map[x, y]
                    elif "D" in dir_map[x, y]:
                        new_map[x, y-3] += map[x, y]
                        new_dir[x, y-3] = dir_map[x, y]
                    elif "L" in dir_map[x, y]:
                        new_map[x-3, y] += map[x, y]
                        new_dir[x-31, y] = dir_map[x, y]
                    elif "R" in dir_map[x, y]:
                        new_map[x+3, y] += map[x, y]
                        new_dir[x+3, y] = dir_map[x, y]
                except IndexError:
                    pass
            else:
                new_map[x-1, y] = max(new_map[x-1, y], map[x, y])+(min(new_map[x-1, y], map[x, y])*0.5)
                new_dir[x-1, y] = direction_merge(new_dir[x-1, y], dir_map[x, y])
    plt.clf()
    
    # to_plot = new_map.transpose()
    # plt.imshow(to_plot)
    # plt.gca().invert_yaxis()
    # plt.colorbar()
    # # plt.show()

    dir_map_color = np.zeros((cWIDTH, cHEIGHT))
    dir_colors = {
        "U":1,
        "D":2,
        "L":3,
        "R":4,
        "":0
    }
    for x in range(cWIDTH):
        for y in range(cHEIGHT):
            dir_map_color[x, y] = dir_colors[dir_map[x, y]]

    to_plot = dir_map_color.transpose()
    plt.imshow(to_plot)
    plt.gca().invert_yaxis()
    plt.colorbar()
    # plt.show()

    plt.savefig(str("./continent_movement/continent_"+str(z)+".png"))

    map = new_map.copy()
    dir_map = new_dir.copy()