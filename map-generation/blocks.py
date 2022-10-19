# import plotly.graph_objs as go
import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.ndimage

# defines the length and the number of levels
length = 100
terrain = np.zeros((length, length))
levels = 20
for j in range(20):
    for k in range(levels, 0, -1):
        radius = random.randrange(levels*2)
        sX = random.randrange(-(levels*2), terrain.shape[0]-(levels*2))
        sY = random.randrange(-(levels*2), terrain.shape[1]-(levels*2))
        for x in range(radius):
            for y in range(radius):
                try:
                    terrain[sX+x, sY+y] += 1
                except IndexError:
                    pass


plt.pcolormesh(terrain, cmap="terrain")
plt.show()

x = 5
sigma = [x, x]
smoothedTerrain = scipy.ndimage.filters.gaussian_filter(terrain, sigma)

ocean = ['rgb(1, 0, 74)', 'rgb(2, 0, 158)', 'rgb(0, 76, 255)', 'rgb(0, 157, 255)', 'rgb(0, 229, 255)', 'rgb(255, 240, 214)']
mountains = ["rgb(0, 2, 138)", "rgb(0, 110, 255)", "rgb(72, 184, 165)", "rgb(11, 110, 0)", "rgb(110, 48, 0)", "rgb(227, 175, 134)", "rgb(255, 255, 255)"]
magic = ["rgb(0, 0, 0)", "rgb(56, 0, 168)", "rgb(93, 0, 255)", "rgb(157, 0, 255)", "rgb(255, 0, 230)", "rgb(255, 153, 187)", "rgb(255, 230, 230)"]

# if imported graph objects
# fig2 = go.Figure(data=[go.Surface(z=smoothedTerrain/5, colorscale=ocean)])
# fig2.show()