from scene import *
import sound
import random
import math
A = Action

SOUNDS = list("ABCDEFG")

class MyScene (Scene):
	def setup(self):
		self.start = SpriteNode('emj:Red_Ring')
		self.start.scale = 2
		
		self.move = SpriteNode('emj:Red_Circle')
		
		self.items = []
	
	def did_change_size(self):
		pass
	
	def update(self):
		for item in self.items:
			item.position = (item.position.x+item.vector[0], item.position.y+item.vector[1])
			if item.position.x <= 0 or item.position.x >= self.size.w:
				item.vector[0] *= -1
				sound.play_effect(item.sound)#'arcade:Hit_3')
			if item.position.y <= 0 or item.position.y >= self.size.h:
				item.vector[1] *= -1
				sound.play_effect(item.sound)#'arcade:Hit_3')
	
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
		item = SpriteNode('emj:Black_Circle')
		item.position = self.start.position
		item.vector = [(self.start.position.x-self.move.position.x)/25, (self.start.position.y-self.move.position.y)/25]
		item.sound = "piano:"+random.choice(SOUNDS)+"3"
		self.add_child(item)
		self.items.append(item)

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
