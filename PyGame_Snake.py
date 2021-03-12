import pygame
from pygame.locals import *
import random
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 800))

def remove_idx(oldList, index):
	newList = []
	for i in range(len(oldList)):
		if i != index:
			newList.append(oldList[i])
	return newList


class Apple:
	def __init__(self, imageFile):
		self.image = pygame.image.load(imageFile)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(1,32)*25
		self.rect.y = random.randrange(1,32)*25
		self.points = 0

	def eaten(self, character):
		if self.rect.colliderect(character.segments[0]):
			self.rect.x = random.randrange(1,32)*25
			self.rect.y = random.randrange(1,32)*25
			self.points += 1
			return True

	def draw(self, character):
		screen.blit(self.image, (self.rect.x, self.rect.y))


class Character:
	def __init__(self, imageFile, startX, startY, xIncrement, yIncrement):
		self.segments = []
		self.image = pygame.image.load(imageFile)
		rect = self.image.get_rect()
		rect.x = startX
		rect.y = startY
		self.dX = xIncrement
		self.dY = yIncrement
		self.direction = ""
		self.segments.append(rect)

	def move(self, points, eaten):
		newX = self.segments[-1].x
		newY = self.segments[-1].y
		if self.direction == "r":
			newX = self.segments[-1].x + self.dX
		elif self.direction == "l":
			newX = self.segments[-1].x - self.dX
		elif self.direction == "u":
			newY = self.segments[-1].y - self.dY
		elif self.direction == "d":
			newY = self.segments[-1].y + self.dY
		self.segments.append(pygame.Rect(newX, newY, 24, 24))
		if eaten:
			pass
		else:
			self.segments = remove_idx(self.segments, 0)

	def right(self):
		if self.direction != "l":
			self.direction = "r"

	def left(self):
		if self.direction != "r":
			self.direction = "l"

	def down(self):
		if self.direction != "u":
			self.direction = "d"

	def up(self):
		if self.direction != "d":
			self.direction = "u"

	def draw(self):
		# print(self.segments)
		for segment in self.segments:
			screen.blit(self.image, (segment.x, segment.y))



class Game:
	def __init__(self):
		self.character = Character("blue.jpg", 400, 400, 25, 25)
		self.fruit = Apple("blue.jpg")

	def grid(self, segments, fruit):
		grid = np.zeros((int(800/25), int(800/25)))
		for segment in segments:
			grid[int(segment.x/25), int(segment.y/25)] = 1
		grid[int(fruit.x/25), int(fruit.y/25)] = 2
		return grid

	def main(self):
		# Variable to keep the main loop running
		running = True
		frames = 0
		# Main loop
		while running:
			print(self.grid(self.character.segments, self.fruit.rect))
			frames += 1
			screen.fill((95, 215, 75))
			for event in pygame.event.get():
				# Did the user hit a key?
				if event.type == KEYDOWN:
					# Was it the Escape key? If so, stop the loop.
					if event.key == K_ESCAPE:
						running = False

					elif event.key == K_UP:
						self.character.up()

					elif event.key == K_DOWN:
						self.character.down()

					elif event.key == K_RIGHT:
						self.character.right()

					elif event.key == K_LEFT:
						self.character.left()
				# Did the user click the window close button? If so, stop the loop.
				elif event.type == QUIT:
					running = False
			if frames%50 == 0:
				eaten = self.fruit.eaten(self.character)
				self.character.move(self.fruit.points, eaten)
			self.fruit.draw(self.character)
			self.character.draw()
			#self.event()
			pygame.display.update()
			if self.character.segments[-1].x > 800 or self.character.segments[-1].x < 0:
				running = False
			elif self.character.segments[-1].y > 800 or self.character.segments[-1].y < 0:
				running = False
			

new_game = Game()
new_game.main()