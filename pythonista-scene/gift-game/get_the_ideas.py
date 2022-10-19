from scene import *
import sound
import random
import math
A = Action


class getTheIdeas (Scene):
	def setup(self):
		#add score
		self.scores = LabelNode('Score: 0')
		self.scores.color = '#000'
		self.scores.position = (100, 700)
		self.add_child(self.scores)
		#General
		self.score = 0
		self.background_color = '#CEF'
		self.totalFrames = 0
		self.changePlayer = 0
		#add button
		self.right = SpriteNode('iow:arrow_right_a_256')
		self.left = SpriteNode('iow:arrow_left_a_256')
		self.right.scale = 0.6
		self.left.scale = 0.6
		self.right.position = (900, 100)
		self.left.position = (100, 100)
		self.add_child(self.right)
		self.add_child(self.left)
		#textures
		self.running = [Texture('run1.PNG'), Texture('run2.PNG')]
		self.light = [Texture('light1.PNG'), Texture('light2.PNG')]
		#add player
		self.player = SpriteNode('run1.PNG')
		self.player.position = (500, 200)
		self.player.scale = 0.5
		self.add_child(self.player)
		#add light
		self.lightbulb1 = SpriteNode('light1.PNG')
		self.lightbulb2 = SpriteNode('light1.PNG')
		self.lightbulb1.position = (random.randrange(1, 9)*100, 700)
		self.lightbulb2.position = (random.randrange(1, 9)*100, 800)
		self.lightbulb1.scale = 0.8
		self.lightbulb2.scale = 0.8
		self.add_child(self.lightbulb1)
		self.add_child(self.lightbulb2)
		#add obstacle
		self.obstacle = SpriteNode('IMG_8823.JPG')
		self.obstacle.position = (random.randrange(1, 9)*100, 700)
		self.obstacle.scale = 0.75
		self.add_child(self.obstacle)
		self.obstacle2 = SpriteNode('IMG_8823.JPG')
		self.obstacle2.position = (random.randrange(1, 9)*100, 900)
		self.obstacle2.scale = 0.75
		self.add_child(self.obstacle2)
		
		self.frames = 0
	
	def did_change_size(self):
		pass
	
	def update(self):
		self.scores.text = 'Score: '+str(self.score)
		self.totalFrames += 1
		#move items
		self.lightbulb1.position = (self.lightbulb1.position.x, self.lightbulb1.position.y-5)
		self.lightbulb2.position = (self.lightbulb2.position.x, self.lightbulb2.position.y-5)
		self.obstacle.position = (self.obstacle.position.x, self.obstacle.position.y-5)
		self.obstacle2.position = (self.obstacle2.position.x, self.obstacle2.position.y-5)
		#change costume
		if self.frames == 10:
			if self.changePlayer == 0:
				self.changePlayer = 1
			else:
				self.changePlayer = 0
			self.frames = 0
			self.player.texture = self.running[self.changePlayer]
			self.lightbulb1.texture = self.light[self.changePlayer]
			self.lightbulb2.texture = self.light[self.changePlayer]
			#Did I get/hit something?
			if self.lightbulb1.bbox.intersects(self.player.bbox) or self.lightbulb1.position.y < 0:
				if self.lightbulb1.position.y > 0:
					self.score += 1
				self.lightbulb1.position = (random.randrange(1, 9)*100, 700)
			elif self.lightbulb2.bbox.intersects(self.player.bbox) or self.lightbulb2.position.y < 0:
				if self.lightbulb2.position.y > 0:
					self.score += 1
				self.lightbulb2.position = (random.randrange(1, 9)*100, 700)
			if self.obstacle.position.y < 0:
				self.obstacle.position = (random.randrange(1, 9)*100, 700)
			if self.player.bbox.intersects(self.obstacle.bbox):
				self.score -= 5
			if self.obstacle2.position.y < 0:
				self.obstacle2.position = (random.randrange(1, 9)*100, 700)
			if self.player.bbox.intersects(self.obstacle2.bbox):
				self.score -= 5
		self.frames += 1
		#print(self.frames)
		return
	
	def touch_began(self, touch):
		#print(touch.location)
		if touch.location.x >= 830 and touch.location.x <= 960 and touch.location.y <= 170 and touch.location.y >= 50:
			self.player.position = (self.player.position.x+100, self.player.position.y)
		if touch.location.x >= 45 and touch.location.x <= 150 and touch.location.y <= 165 and touch.location.y >= 50:
			self.player.position = (self.player.position.x-100, self.player.position.y)
		
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(getTheIdeas(), show_fps=False)
