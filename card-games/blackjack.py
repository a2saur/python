import shuffle_deck
from console import clear
import money_graph as mg
import random


def toString(myList, seperator):
	string = ""
	for x in myList:
		string += x
		string += seperator
	return string


def get_deck():
	shuffle_deck.shuffle()
	deck = open("cards.txt",'r').read()
	cards = deck.split("\n")
	if len(cards) > 52:
		last = cards.pop()
	if last != '':
		print("ERROR")
	return cards


def display(d, p1, end):
	clear()
	p1Hand = toString(p1, " ")
	if end:
		print("Dealer:")
		dEnd = toString(d, " ")
		print(dEnd)
		print("--")
		print("You:")
		print(p1Hand)
	else:
		print("Dealer:")
		print(d[0], "X")
		print("--")
		print("You:")
		print(p1Hand)


def get_amount(hand):
	total = 0
	aces = 0
	for card in hand:
		if card in ["J", "Q", "K"]:
			total += 10
		elif card == "A":
			aces += 1
		else:
			total += int(card)
	for x in range(aces):
		if total+11 > 21:
			total += 1
		else:
			total += 11
	return total


def bust(hand, dealer):
	total = get_amount(hand)
	if total > 21:
		if dealer:
			print("DEALER BUST")
		else:
			print("BUST")
		return True
	else:
		return False


def deal(cards):
	c1 = cards[0]
	c2 = cards[1]
	c3 = cards[2]
	c4 = cards[3]
	
	cards.remove(c1)
	cards.remove(c2)
	cards.remove(c3)
	cards.remove(c4)
	
	dealHand = [c1, c3]
	p1Hand = [c2, c4]
	
	return [cards, dealHand, p1Hand]


def deal_move(dealer, cards):
	while get_amount(dealer) <= 16:
		dealer.append(cards[0])
		cards.remove(cards[0])
		if bust(dealer, True):
			return [dealer, cards]
	return [dealer, cards]


def p1_move():
	while True:
		ui = input("Your Move (Stand is s, Hit is h): ")
		if ui.lower() == "s":
			#Stand
			return False
		elif ui.lower() == "h":
			#Hit
			return True


def round(cards, money):
	if money < 2:
		print("You have no more betting money -- and a gambling problem")
		mg.graph()
		return money
	clear()
	print("Your Money Amount: "+str(money))
	while True:
		try:
			p1Bet = random.randrange(money-10)#int(input("Bet amount: "))
			if p1Bet < 2:
				print("Minimum bet is 2")
			elif p1Bet > money:
				print("That\'s more money than you have")
			else:
				break
		except ValueError:
			print("Not a valid value -- Please type in a whole number")
	#print(len(cards))
	if len(cards) <= 3:
		return money
	temp = deal(cards)
	cards = temp[0]
	dealHand = temp[1]
	p1Hand = temp[2]
	
	display(dealHand, p1Hand, False)
	while True:
		if bust(p1Hand, False):
			break
		else:
			pass
		p1Move = p1_move()
		if p1Move:
			p1Hand.append(cards[0])
			cards.remove(cards[0])
			display(dealHand, p1Hand, False)
		else:
			temp = deal_move(dealHand, cards)
			dealHand = temp[0]
			cards = temp[1]
			break
	display(dealHand, p1Hand, True)
	if bust(p1Hand, False):
		print("--YOU LOSE--")
		money -= p1Bet
	elif bust(dealHand, True):
		print("--YOU WIN--")
		money += p1Bet
	else:
		if get_amount(p1Hand)>get_amount(dealHand):
			print("--YOU WIN--")
			money += p1Bet
		elif get_amount(p1Hand)<get_amount(dealHand):
			print("--YOU LOSE--")
			money -= p1Bet
		else:
			print("--TIE--")
	open("money.txt", "a").write(str(money))
	open("money.txt", "a").write(", ")
	print("Your Money: ", money)
	input("Press enter when ready")
	if round(cards, money) != "":
		return money



open("money.txt", "w").write("")
cards = get_deck()
startMoney = 1000
money = round(cards, startMoney)
ui = input("Press q to quit")
while ui.lower() != "q":
	cards = get_deck()
	money = round(cards, money)
	ui = input("Press q to quit")
