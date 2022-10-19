from scene import *
import sound
import random
import math
A = Action

WINNINGS = {'rock':'paper', 'paper':'scissor', 'scissor':'rock'}
IMAGES = {'rock':'emj:Moon_2', 'paper':'emj:Newspaper', 'scissor':'emj:Scissors'}

class MyScene (Scene):
	def setup(self):
		self.start = SpriteNode('emj:Red_Ring')
		self.start.scale = 2
		
		self.move = SpriteNode('emj:Red_Circle')
		
		self.items = []
		for x in range(20):
			x = random.choice(list(WINNINGS.keys()))
			item = SpriteNode(IMAGES[x])
			item.position = (random.randrange(self.size.w), random.randrange(self.size.h))
			item.vector = [random.randrange(-5, 5), random.randrange(-5, 5)]
			item.type = x
			self.add_child(item)
			self.items.append(item)
	
	def did_change_size(self):
		pass
	
	def update(self):
		for item in self.items:
			item.position = (item.position.x+item.vector[0], item.position.y+item.vector[1])
			if item.position.x <= 0 or item.position.x >= self.size.w:
				item.vector[0] *= -1
			if item.position.y <= 0 or item.position.y >= self.size.h:
				item.vector[1] *= -1
			for item2 in self.items:
				if item.position in item2.bbox and item.position != item2.position:
					item.vector[0] *= -1
					item.vector[1] *= -1
					if item2.type == WINNINGS[item.type]:
						item.type = item2.type
						item.texture = Texture(IMAGES[item.type])
	
	def touch_began(self, touch):
		self.start.position = touch.location
		self.add_child(self.start)
		self.move.position = touch.location
		self.add_child(self.move)
	
	def touch_moved(self, touch):
		self.move.position = touch.location
	
	def touch_ended(self, touch):
		self.start.remove_from_parent()
		self.move.remove_from_parent()
		
		x = random.choice(list(WINNINGS.keys()))
		item = SpriteNode(IMAGES[x])
		item.position = self.start.position
		item.vector = [(self.start.position.x-self.move.position.x)/50, (self.start.position.y-self.move.position.y)/50]
		item.type = x
		self.add_child(item)
		self.items.append(item)

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
