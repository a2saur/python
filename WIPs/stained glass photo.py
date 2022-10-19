from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from math import sqrt

class Filler():
 def __init__(self, image):
   self.image = image

 # fills part of an image starting at [location] with [colorVal] until it hits a pixel with [outlineVal]
 def fill_small(self, location, outlineVal=[0,0,0], colorVal=[255, 0, 0]):
   grid = [(1,0), (0,-1), (0,1), (-1,0)]
   for dL in grid:
     currentLoc = (location[0]+dL[0], location[1]+dL[1])
     try:
       if self.image[currentLoc[0], currentLoc[1], 0] == 0 and self.image[currentLoc[0], currentLoc[1], 1] == 0 and self.image[currentLoc[0], currentLoc[1], 0] == 0:
         # don't go further
         return
       elif isEqual(self.image[currentLoc[0], currentLoc[1]], colorVal):
         pass
       else:
         # fill and send this as a location
         self.image[currentLoc[0], currentLoc[1]] = colorVal
         self.fill_small(currentLoc, outlineVal, colorVal)
     except IndexError:
       pass

 # gives back the image
 def get_image(self):
   return self.image

 # shows the image
 def show_image(self):
   plt.clf()
   plt.imshow(grid)
   plt.axis('off')
   plt.show()

def fill_array(array, position, value, default_value=-1, line_value=0):
	if array[position[0], position[1], 0] == default_value and array[position[0], position[1], 0] != line_value:
		array[position[0], position[1], 0] = value[0]
		array[position[0], position[1], 1] = value[1]
		array[position[0], position[1], 2] = value[2]
		array = fill_array(array, [position[0]+1, position[1]], value, default_value, line_value)
		array = fill_array(array, [position[0]-1, position[1]], value, default_value, line_value)
		array = fill_array(array, [position[0], position[1]+1], value, default_value, line_value)
		array = fill_array(array, [position[0], position[1]-1], value, default_value, line_value)
		return array
	else:
		return array


image = Image.open("koala.jpg")
pixels = list(image.getdata())
width, height = image.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]


# gets the image
image = Image.open("koala.jpg")
pixels = list(image.getdata())
width, height = image.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
print("Got image")
# transfers image to a numpy array
outline = np.empty([height, width, 3], dtype=np.uint8)
for x in range(0, outline.shape[0]):
    for y in range(0, outline.shape[1]):
        outline[x, y, 0] = pixels[x][y][0]
        outline[x, y, 1] = pixels[x][y][1]
        outline[x, y, 2] = pixels[x][y][2]
print("Transferred to np array")

for x in range(randrange(int(width/100), int(width/25))):
	currentX = 0
	currentY = 0
	pointA = [randrange(width), 0]
	pointB = [randrange(width), height-1]
	dX = pointA[0]-pointB[0]
	dY = pointA[1]-pointB[1]
	hyp = sqrt((dX**2)+(dY**2))
	for y in range(int(hyp)):
		currentX += dX/hyp
		currentY += dY/hyp
		outline[pointB[0]+int(currentX), pointB[1]+int(currentY)] = [0,0,0]
	outline[pointB[0], pointB[1]] = [0, 0, 0]
	outline[pointA[0], pointA[1]] = [0, 0, 0]

for x in range(randrange(int(width/100), int(width/25))):
	currentX = 0
	currentY = 0
	pointA = [0, randrange(height)]
	pointB = [width-1, randrange(height)]
	dX = pointA[0]-pointB[0]
	dY = pointA[1]-pointB[1]
	hyp = sqrt((dX**2)+(dY**2))
	for y in range(int(hyp)):
		currentX += dX/hyp
		currentY += dY/hyp
		outline[pointB[0]+int(currentX), pointB[1]+int(currentY)] = 0


# border
for x in range(width):
	outline[x, 0] = [0, 0, 0]
	outline[x, height-1] = [0, 0, 0]
for y in range(height):
	outline[0, y] = [0, 0, 0]
	outline[width-1, y] = [0, 0, 0]


# pX = 0
# pY = 0
# for x in range(2):
# 	while True:
# 		pX = randrange(width)
# 		pY = randrange(height)
# 		if outline[pX, pY, 0] != 0:
# 			break
# 	outline = fill_array(outline, [pX, pY], pixels[pX][pY], 255, 0)

# fills the image using the [Filler] class
filler = Filler(outline)
prevLocation = [0, 0]
# selects the first fillable spot
while True:
    prevLocation[0] += 1
    if prevLocation[0] >= grid.shape[0]:
        prevLocation[1] += 1
        prevLocation[0] = 0
    try:
        if outline[prevLocation[0], prevLocation[1], 0] == 0:
            pass
        else:
            filler.fill_small(prevLocation, colorVal=outline[prevLocation[0], prevLocation[1]])
    except IndexError:
        break
print("Filled")
filler.show_image()

# plt.clf()
# plt.imshow(outline)
# #plt.axis('off')
# plt.show()
