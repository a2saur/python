def shoot(r):
	print("Computer Cards\n-\n-\n-")


def war():
	print("pew pew pew! war has been declared! pew pew pew pew pew pew!")
	cFile = open('computerhalfofdeck.txt', 'r')
	text = cFile.read()
	cCard = text.split(', ')
	pFile = open('playerhalfofdeck.txt', 'r')
	text = pFile.read()
	pCard = text.split(', ')
	r = 0
	con = ""
	while con != "Q" or "q":
		if con == "S" or "s":
			print("Computer’s cards: ", len(cCard), "Player’s cards: ", len(pCard))
		print("Computer Card - " + cCard[r])
		print("Player Card - " + pCard[r])
		if pCard[r] > cCard[r]:
			pCard += cCard[r]
			lostCard = str(cCard[r])
			cCard.remove(lostCard)
		elif pCard[r] < cCard[r]:
			cCard += pCard[r]
			lostCard = str(pCard[r])
			pCard.remove(lostCard)
		r = r + 1
		if len(pCard) > len(cCard):
			a = len(cCard)
		elif len(pCard) < len(cCard):
			a = len(pCard)
		else:
			a = 26
		if r >= a:
			r = 0
		con = input("")

war()
