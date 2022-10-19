from scene import *
import sound
import random
import math
A = Action

NUM_LAYERS = 3


def touch_diff(touch1, touch2):
	return abs(math.sqrt((touch1.location.x-touch2.location.x)**2+(touch1.location.y-touch2.location.y)**2))

def prev_vs_now(touch1):
	return math.sqrt((touch1.location.x-touch1.prev_location[0])**2+(touch1.location.y-touch1.prev_location[1])**2)

def prevs_diff(touch1, touch2):
	return math.sqrt((touch1.prev_location[0]-touch2.prev_location[0])**2+(touch1.prev_location[1]-touch2.prev_location[1])**2)

class MyScene (Scene):
	def setup(self):
		self.layers = []
		self.layer_depths = []
		for x in range(1, NUM_LAYERS+1):
			image_name = "layer"+str(x)+".PNG"
			layer = SpriteNode(image_name)
			layer.position = (self.size.w/2, self.size.h/2)
			layer.scale = 0.5
			self.add_child(layer)
			self.layers.append(layer)
			self.layer_depths.append(100+(NUM_LAYERS*100)-(x*100))
	
	def did_change_size(self):
		pass
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		self.prev_touch = touch.location
		
	
	def touch_moved(self, touch):
		if len(self.touches.values()) == 1:
			dX = touch.location.x-self.prev_touch.x
			dY = touch.location.y-self.prev_touch.y
			for x in range(NUM_LAYERS):
				self.layers[x].position = (self.layers[x].position.x+(dX/self.layer_depths[x])*100, self.layers[x].position.y+(dY/self.layer_depths[x])*100)
			self.prev_touch = touch.location
		elif len(self.touches.values()) == 2:
			for x in range(NUM_LAYERS):
				ts = list(self.touches.values())
				#print(ts[0].prev_location)
				self.layers[x].scale += (touch_diff(ts[0], ts[1])-prevs_diff(ts[0], ts[1]))/1000#100
				if self.layers[x].scale < 0:
					self.layers[x].scale = 0
				dX = ((ts[0].location.x-ts[0].prev_location[0])+(ts[1].location.x-ts[1].prev_location[0]))/2
				dY = ((ts[0].location.y-ts[0].prev_location[1])+(ts[1].location.y-ts[1].prev_location[1]))/2
				self.layers[x].position = (self.layers[x].position.x+(dX/self.layer_depths[x])*100, self.layers[x].position.y+(dY/self.layer_depths[x])*100)
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
