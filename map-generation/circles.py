import numpy as np
from random import randrange
import matplotlib.pyplot as plt
from blur import blur

width = 500
height = 500
max_block_radius = int((width+height)/20)
max_num_blocks = 250

map = np.zeros((width, height))

for b in range(randrange(int(max_num_blocks/2), max_num_blocks)):
	r = randrange(int(max_block_radius/2), max_block_radius)
	startX = randrange(width-max_block_radius)
	startY = randrange(height-max_block_radius)
	for x in range(startX-r, startX+r):
		for y in range(startY-r, startY+r):
			dist = ((x-startX)**2 + (y-startY)**2)**0.5
			if dist < r:
				if 0 < x < width and 0 < y < height:
					map[x, y] += 1
	
plt.imshow(blur(map, 10), cmap="terrain")
plt.gca().invert_yaxis()
plt.colorbar()
plt.show()