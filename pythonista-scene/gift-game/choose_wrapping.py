from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):
		#self.shoot = SpriteNode('IMG_8872.PNG')
		self.shoot = []
		self.wrappings1 = SpriteNode('IMG_8876.JPG')
		self.wrappings2 = SpriteNode('IMG_8877.JPG')
		self.wrappings3 = SpriteNode('IMG_8878.JPG')
		self.wrappings1.position = (100, 700)
		self.wrappings2.position = (500, 700)
		self.wrappings3.position = (800, 700)
		self.wrappings1.scale = 0.75
		self.wrappings2.scale = 0.75
		self.wrappings3.scale = 0.75
		self.wrappings = [self.wrappings1, self.wrappings2, self.wrappings3]
		self.add_child(self.wrappings1)
		self.add_child(self.wrappings2)
		self.add_child(self.wrappings3)
		self.directions = [1, 1, 1]
	
	def did_change_size(self):
		pass
	
	def update(self):
		for shot in self.shoot:
			shot.position = (shot.position.x, shot.position.y+10)
			if shot.position.y > 1000:
				shot.remove_from_parent()
				self.shoot.remove(shot)
			if shot.bbox.intersects(>)
		for x in range(len(self.wrappings)):
			if self.directions[x] == 1:
				self.wrappings[x].position = (self.wrappings[x].position.x+5, self.wrappings[x].position.y)
			elif self.directions[x] == -1:
				self.wrappings[x].position = (self.wrappings[x].position.x-5, self.wrappings[x].position.y)
				
			if self.wrappings[x].position.x > 900:
				self.directions[x] = -1
				#print(self.directions[x])
			elif self.wrappings[x].position.x < 100:
				self.directions[x] = 1
				#print(self.directions[x])
	
	def touch_began(self, touch):
		#self.shoot = SpriteNode('IMG_8872.PNG')
		shot = SpriteNode('IMG_8872.PNG')
		shot.position = (touch.location.x, 0)
		self.add_child(shot)
		self.shoot.append(shot)
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
