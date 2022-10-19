from scene import *
import sound
import random
import math
A = Action
standing_texture = Texture('plf:AlienGreen_front')
walking_textures = [Texture('plf:AlienGreen_walk1'), Texture('plf:AlienGreen_walk1'), Texture('plf:AlienGreen_walk1'), Texture('plf:AlienGreen_walk1'), Texture('plf:AlienGreen_walk2'), Texture('plf:AlienGreen_walk2'), Texture('plf:AlienGreen_walk2'), Texture('plf:AlienGreen_walk2')]

walking_textures2 = [Texture('plf:AlienYellow_walk1'), Texture('plf:AlienYellow_walk1'), Texture('plf:AlienYellow_walk1'), Texture('plf:AlienYellow_walk1'), Texture('plf:AlienYellow_walk2'), Texture('plf:AlienYellow_walk2'), Texture('plf:AlienYellow_walk2'), Texture('plf:AlienYellow_walk2')]

jelly_textures = [Texture('plf:Enemy_SlimeBlock'), Texture('plf:Enemy_SlimeBlock_move')]
bee_textures = [Texture('plf:Enemy_Bee'), Texture('plf:Enemy_Bee_move')]
barnacle_textures = [Texture('plf:Enemy_Barnacle'), Texture('plf:Enemy_Barnacle_attack')]

class ChangeCostumes (Scene):
	def cJellies(self):
		if self.costume == 10:
			for jelly in list(self.jellies):
				jelly.texture = jelly_textures[0]
				if jelly.bbox.intersects(self.player.bbox):
					self.jump = 'UP'
				if jelly.bbox.intersects(self.player2.bbox):
					self.jump2 = 'UP'
		elif self.costume == 20:
			self.costume = 0
			for jelly in list(self.jellies):
				jelly.texture = jelly_textures[1]
				if jelly.bbox.intersects(self.player.bbox):
					self.jump = 'UP'
				if jelly.bbox.intersects(self.player2.bbox):
					self.jump2 = 'UP'
	
	def cBees(self):
		if self.costume == 5 or self.costume == 15:
			for k in range(len(list(self.bees))):
				bee = list(self.bees)[k]
				bee.texture = bee_textures[0]
				cpx1 = bee.position.x-self.player.position.x
				cpx2 = bee.position.x-self.player2.position.x
				if abs(cpx1)<abs(cpx2): #bee's x position is closer to player1
					if abs(cpx1)==cpx1: #x position is ahead of player1
						bee.position = (bee.position.x-7, bee.position.y)
					else:
						bee.position = (bee.position.x+7, bee.position.y)
				else:
					if abs(cpx2)==cpx2: #x position is ahead of player1
						bee.position = (bee.position.x-7, bee.position.y)
					else:
						bee.position = (bee.position.x+7, bee.position.y)
				bee2 = list(self.bees2)[k]
				bee2.position = (1024-bee.position.x, 770-bee.position.y)
				if self.player.bbox.intersects(bee.bbox):
					self.aaa = True
				if self.player2.bbox.intersects(bee.bbox):
					self.aaa2 = True
		
		elif self.costume == 20 or self.costume == 10:
			for k in range(len(list(self.bees))):
				bee = list(self.bees)[k]
				bee.texture = bee_textures[1]
				cpx1 = bee.position.x-self.player.position.x
				cpx2 = bee.position.x-self.player2.position.x
				if abs(cpx1)<abs(cpx2): #bee's x position is closer to player1
					if abs(cpx1)==cpx1: #x position is ahead of player1
						bee.position = (bee.position.x-7, bee.position.y)
					else:
						bee.position = (bee.position.x+7, bee.position.y)
				else:
					if abs(cpx2)==cpx2: #x position is ahead of player1
						bee.position = (bee.position.x-7, bee.position.y)
					else:
						bee.position = (bee.position.x+7, bee.position.y)
				bee2 = list(self.bees2)[k]
				bee2.position = (1024-bee.position.x, 770-bee.position.y)
				
				cpy1 = bee.position.y-self.player.position.y
				cpy2 = bee.position.y-self.player2.position.y
				if abs(cpy1)<abs(cpy2): #bee's x position is closer to player1
					if abs(cpy1)==cpy1: #x position is ahead of player1
						bee.position = (bee.position.x, bee.position.y-7)
					else:
						bee.position = (bee.position.x, bee.position.y+7)
				else:
					if abs(cpy2)==cpy2: #x position is ahead of player1
						bee.position = (bee.position.x, bee.position.y-7)
					else:
						bee.position = (bee.position.x, bee.position.y+7)
				bee2 = list(self.bees2)[k]
				bee2.position = (1024-bee.position.x, 770-bee.position.y)
				
				if self.player.bbox.intersects(bee.bbox):
					self.aaa = True
				if self.player2.bbox.intersects(bee.bbox):
					self.aaa2 = True

class CreateItems (Scene):
	def make_jellies(self, position1):
		jelly3 = SpriteNode('plf:Enemy_SlimeBlock')
		jelly3.position = (position1, 625)
		jelly3.y_scale = -1
		self.add_child(jelly3)
		self.toMoveUp.append(jelly3)
		self.jellies.append(jelly3)
		
		jelly4 = SpriteNode('plf:Enemy_SlimeBlock')
		jelly4.position = (1024-position1, 150)
		jelly4.y_scale = 1
		self.add_child(jelly4)
		self.toMove.append(jelly4)
		self.jellies.append(jelly4)
	
	def make_bees(self, x, y):
		jelly3 = SpriteNode('plf:Enemy_Bee')
		jelly3.position = (x, y)
		jelly3.y_scale = -1
		self.add_child(jelly3)
		self.toMoveUp.append(jelly3)
		self.bees2.append(jelly3)
		
		jelly4 = SpriteNode('plf:Enemy_Bee_move')
		jelly4.position = (1024-x, 770-y)
		jelly4.y_scale = 1
		self.add_child(jelly4)
		self.toMove.append(jelly4)
		self.bees.append(jelly4)

class MyScene (Scene):
	def setup(self):
		self.aaa = False
		self.aaa2 = False
		self.aat = 0
		self.at2 = 0
		self.costume = 0
		self.jump = 'none'
		self.change = 0
		#make lists
		self.items = {'Jellies': 0, }
		self.bees = []
		self.bees2 = []
		self.jellies = []
		self.toMove = []
		self.toMoveUp = []
		#add ground
		self.background = SpriteNode('IMG_8974.JPG')
		self.background.position = (500, -100)
		self.add_child(self.background)
		#set background color
		self.background_color = '#4fc1ff'
		#add player
		self.player = SpriteNode('plf:AlienGreen_front')
		self.player.position = (100, 200)
		self.add_child(self.player)
		#add player2
		self.player2 = SpriteNode('plf:AlienYellow_front')
		self.player2.position = (100, 200)
		self.add_child(self.player2)
		#add left button
		self.leftButton = SpriteNode('iob:arrow_left_a_256')
		self.leftButton.scale = 0.4
		self.leftButton.position = (50, 75)
		self.add_child(self.leftButton)
		#add right button
		self.rightButton = SpriteNode('iob:arrow_right_a_256')
		self.rightButton.scale = 0.4
		self.rightButton.position = (150, 75)
		self.add_child(self.rightButton)
		#add jump button
		self.jumpButton = SpriteNode('iob:arrow_up_a_256')
		self.jumpButton.scale = 0.4
		self.jumpButton.position = (900, 75)
		self.add_child(self.jumpButton)
		
		#add second view
		self.jump2 = 'none'
		self.change2 = 0
		#add ground
		self.background = SpriteNode('IMG_8974.JPG')
		self.background.position = (500, 875)
		self.background.y_scale = -1
		self.add_child(self.background)
		#add player
		self.player3 = SpriteNode('plf:AlienGreen_front')
		self.player3.y_scale = -1
		self.player3.position = (100, 575)
		self.add_child(self.player3)
		#add player2
		self.player4 = SpriteNode('plf:AlienYellow_front')
		self.player4.y_scale = -1
		self.player4.position = (100, 575)
		self.add_child(self.player4)
		#add left button
		self.rightButton2 = SpriteNode('iob:arrow_left_a_256')
		self.rightButton2.scale = 0.4
		self.rightButton2.position = (50, 700)
		self.add_child(self.rightButton2)
		#add right button
		self.leftButton2 = SpriteNode('iob:arrow_right_a_256')
		self.leftButton2.scale = 0.4
		self.leftButton2.position = (150, 700)
		self.add_child(self.leftButton2)
		#add jump button
		self.jumpButton2 = SpriteNode('iob:arrow_up_a_256')
		self.jumpButton2.scale = 0.4
		self.jumpButton2.y_scale = -0.4
		self.jumpButton2.position = (900, 700)
		self.add_child(self.jumpButton2)
		
		#add creatures
		CreateItems.make_jellies(self, 500)
		CreateItems.make_bees(self, 700, 500)
	
	def did_change_size(self):
		pass
	
	def update(self):
		if self.aaa == True:
			self.aat += 1
		if self.aat == 300:
			self.aat = 0
			self.aaa = False
		
		if self.aaa2 == True:
			self.at2 += 1
		if self.at2 == 300:
			self.at2 = 0
			self.aaa2 = False
		#jumping for player 1
		if self.jump == 'up':
			self.player.position = (self.player.position.x, self.player.position.y+5)
			if self.player.position.y > 300 and self.aaa == False:
				self.jump = 'down'
			elif self.aaa == True:
				if self.player.position.y > 200:
					self.jump = 'down'
		elif self.jump == 'down':
			self.player.position = (self.player.position.x, self.player.position.y-5)
			if self.player.position.y == 200:
				self.jump = 'none'
		elif self.jump == 'UP':
			self.player.position = (self.player.position.x, self.player.position.y+5)
			if self.player.position.y > 500 and self.aaa == False:
				self.jump = 'DOWN'
			elif self.aaa == True:
				if self.player.position.y > 400:
					self.jump = 'DOWN'
		elif self.jump == 'DOWN':
			self.player.position = (self.player.position.x, self.player.position.y-5)
			if self.player.position.y == 200:
				self.jump = 'none'
		#Have buttons been touched?
		for Touch in self.touches.values():
			if Touch.location in self.leftButton.bbox: # if button is touched
				self.player.x_scale = -1
				self.change += 1
				if self.change == len(walking_textures):
					self.change = 0
				self.player.texture = walking_textures[self.change]
				newX = self.player.position.x-5
				if newX >= 0 and newX <= 512:
					self.player.position = (newX, self.player.position.y)
				elif newX > 512:
					for item in list(self.toMove):
						item.position = (item.position.x-5, item.position.y)
					for item in list(self.toMoveUp):
						item.position = (item.position.x+5, item.position.y)
			if Touch.location in self.rightButton.bbox: # if button is touched
				self.player.x_scale = 1
				self.change += 1
				if self.change == len(walking_textures):
					self.change = 0
				self.player.texture = walking_textures[self.change]
				newX = self.player.position.x+5
				if newX >= 0 and newX <= 512:
					self.player.position = (newX, self.player.position.y)
				elif newX > 512:
					for item in list(self.toMove):
						item.position = (item.position.x-5, item.position.y)
					for item in list(self.toMoveUp):
						item.position = (item.position.x+5, item.position.y)
			if Touch.location in self.jumpButton.bbox: # if button is touched
				if self.player.position.y == 200:
					self.jump = 'up'
	
		#player 2
		#jumping
		if self.jump2 == 'up':
			self.player2.position = (self.player2.position.x, self.player2.position.y+5)
			if self.player2.position.y > 300 and self.aaa2 == False:
				self.jump2 = 'down'
			elif self.aaa2 == True:
				if self.player2.position.y > 200:
					self.jump2 = 'down'
		elif self.jump2 == 'down':
			self.player2.position = (self.player2.position.x, self.player2.position.y-5)
			if self.player2.position.y == 200:
				self.jump2 = 'none'
		elif self.jump2 == 'UP':
			self.player2.position = (self.player2.position.x, self.player2.position.y+5)
			if self.player2.position.y > 500 and self.aaa2 == False:
				self.jump2 = 'DOWN'
			elif self.aaa2 == True:
				if self.player2.position.y > 400:
					self.jump2 = 'DOWN'
		elif self.jump2 == 'DOWN':
			self.player2.position = (self.player2.position.x, self.player2.position.y-5)
			if self.player2.position.y == 200:
				self.jump2 = 'none'
		#button touched?
		for Touch in self.touches.values():
			if Touch.location in self.leftButton2.bbox: # if button is touched
				self.player2.x_scale = -1
				self.change2 += 1
				if self.change2 == len(walking_textures2):
					self.change2 = 0
				self.player2.texture = walking_textures2[self.change2]
				newX = self.player2.position.x-5
				if newX >= 0 and newX <= 512:
					self.player2.position = (newX, self.player2.position.y)
				elif newX > 512:
					for item in list(self.toMove):
						item.position = (item.position.x-5, item.position.y)
					for item in list(self.toMoveUp):
						item.position = (item.position.x+5, item.position.y)
			if Touch.location in self.rightButton2.bbox: # if button is touched
				self.player2.x_scale = 1
				self.change2 += 1
				if self.change2 == len(walking_textures2):
					self.change2 = 0
				self.player2.texture = walking_textures2[self.change2]
				newX = self.player2.position.x+5
				if newX >= 0 and newX <= 512:
					self.player2.position = (newX, self.player2.position.y)
				elif newX > 512:
					for item in list(self.toMove):
						item.position = (item.position.x-5, item.position.y)
					for item in list(self.toMoveUp):
						item.position = (item.position.x+5, item.position.y)
			if Touch.location in self.jumpButton2.bbox: # if button is touched
				if self.player2.position.y == 200:
					self.jump2 = 'up'
		#update screen
		self.player3.position = (1021-self.player.position.x, 768-self.player.position.y)
		self.player3.texture = self.player.texture
		self.player3.x_scale = self.player.x_scale*-1
		self.player4.position = (1021-self.player2.position.x, 768-self.player2.position.y)
		self.player4.texture = self.player2.texture
		self.player4.x_scale = self.player2.x_scale*-1
		
		#update creatures
		self.costume += 1
		ChangeCostumes.cBees(self)
		ChangeCostumes.cJellies(self)
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
