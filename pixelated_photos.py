# IMPORTING
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from math import *

# a function that checks if two colors (rgb) are equal
def isEqual(arr1, arr2):
    if arr1[0] == arr2[0]:
        if arr1[1] == arr2[1]:
            if arr1[2] == arr2[2]:
                return True

# the filler class takes an image with a grid and fills it in with the first color
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


# takes a grid and adds lines to it
def add_grid(image, numLines=10):
    xStep = 25
    yStep = 25
    for x in range(0, grid.shape[0], xStep):
        for y in range(0, grid.shape[1]):
            image[x, y] = [0, 0, 0]
    for x in range(0, grid.shape[0]):
        for y in range(0, grid.shape[1], yStep):
            image[x, y] = [0, 0, 0]
    return image

# gets the image
image = Image.open("koala.jpg")
pixels = list(image.getdata())
width, height = image.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
print("Got image")
# transfers image to a numpy array
grid = np.empty([height, width, 3], dtype=np.uint8)
for x in range(0, grid.shape[0]):
    for y in range(0, grid.shape[1]):
        grid[x, y, 0] = pixels[x][y][0]
        grid[x, y, 1] = pixels[x][y][1]
        grid[x, y, 2] = pixels[x][y][2]
grid = add_grid(grid)
print("Transferred to np array")
# fills the image using the [Filler] class
filler = Filler(grid)
prevLocation = [0, 0]
# selects the first fillable spot
while True:
    prevLocation[0] += 1
    if prevLocation[0] >= grid.shape[0]:
        prevLocation[1] += 1
        prevLocation[0] = 0
    try:
        if grid[prevLocation[0], prevLocation[1], 0] == 0:
            pass
        else:
            filler.fill_small(prevLocation, colorVal=grid[prevLocation[0], prevLocation[1]])
    except IndexError:
        break
print("Filled")
filler.show_image()
