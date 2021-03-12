import random


class Board():
	board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

	def __init__(self, numbersOn=False):
		self.numbersOn = numbersOn

	def display(self):
		string = ""
		for x in range(3):
			for y in range(1, 4):
				if self.board[(x*3)+y-1] == " ":
					if self.numbersOn:
						string += str((x*3)+y)
					else:
						string += " "
				else:
					string += self.board[(x*3)+y-1]
				if y != 3:
					string += "|"
			if x != 2:
				string += "\n-----\n"
		print(string)
		return string

	def get_board(self):
		return self.board

	def reset(self):
		self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

	def check_win(self):
		locations = [
			(0,1,2),
			(3,4,5),
			(6,7,8), # ^ all horizontals
			(0,3,6),
			(1,4,7),
			(2,5,8), # ^ all verticals
			(0,4,8),
			(2,4,6), # ^ all diagnols
		]

		if " " not in self.board:
			return "No one"

		for l in locations:
			if self.board[l[0]] == self.board[l[1]] == self.board[l[2]] != " ":
				return self.board[l[0]]
		else:
			return False

	def add_item(self, player, location):
		self.board[location] = player.get_marker()

	def spot_available(self, location):
		if self.board[location] == " ":
			return True
		else:
			return False

	def get_available_spots(self):
		spots = []
		for x in range(len(self.board)):
			if self.board[x] == " ":
				spots.append(x)
		return spots



class Player():
	def __init__(self, notAvailable=["1","2","3","4","5","6","7","8","9"]):
		while True:
			marker = input("What is your marker? ")
			if marker not in notAvailable:
				break
		self.marker = marker

	def get_move(self, board):
		while True:
			try:
				location = int(input("What is your move? "))
				if location > 9:
					print("Please put a number less than 10")
					int("Error Time!")
				if location < 1:
					print("Please put a number greater than 0")
					int("Error Time!")
				if not board.spot_available(location-1):
					print("Spot Unavailable")
					int("Error Time!")
				break
			except ValueError:
				print("Please put a number in")
		board.add_item(self, location-1)

	def get_marker(self):
		return self.marker



class Computer():
	def __init__(self, notAvailable=["1","2","3","4","5","6","7","8","9"], compType=0):
		while True:
			marker = input("What is the computer\'s marker? ")
			if marker not in notAvailable:
				break
		self.marker = marker
		self.computerType = compType

	def randomMove(self, availSpots):
		return random.choice(availSpots)

	def randomCheckMove(self, board):
		locations = [
			(0,1,2),
			(3,4,5),
			(6,7,8), # ^ all horizontals
			(0,3,6),
			(1,4,7),
			(2,5,8), # ^ all verticals
			(0,4,8),
			(2,4,6), # ^ all diagnols
		]
		for locSet in locations:
			for x in range(3):
				for y in range(3):
					if board.get_board()[locSet[x]] == board.get_board()[locSet[y]] != " " and x != y:
						for z in range(3):
							if z != x and z != y:
								return locSet[z]
		return self.randomMove(board.get_available_spots())

	def get_move(self, board):
		if self.computerType == 0: # random
			board.add_item(self, self.randomMove(board.get_available_spots()))
		elif self.computerType == 1: # random with check win
			board.add_item(self, self.randomCheckMove(board))

	def get_marker(self):
		return self.marker



class Game():
	def __init__(self):
		self.board = Board(numbersOn=True)
		if random.randrange(2) == 0:
			self.player1 = Player()
			self.player2 = Computer(["1","2","3","4","5","6","7","8","9", self.player1.get_marker()], compType=1)
		else:
			self.player2 = Player()
			self.player1 = Computer(["1","2","3","4","5","6","7","8","9", self.player1.get_marker()], compType=1)

	def game(self):
		while True:
			self.board.display()
			print(self.player1.get_marker()+" Move")
			self.player1.get_move(self.board)
			if self.board.check_win() != False:
				print(self.board.check_win()+" Wins!!!")
				break

			self.board.display()
			print(self.player2.get_marker()+" Move")
			self.player2.get_move(self.board)
			if self.board.check_win() != False:
				print(self.board.check_win()+" Wins!!!")
				break

	def main(self):
		while True:
			self.board.reset()
			self.game()
			if input("Type q to quit or anything else to continue: ") == "q":
				print("Thanks for playing!")
				return



myGame = Game()
myGame.game()