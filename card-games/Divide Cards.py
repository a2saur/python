computerHand = open('computerhalfofdeck.txt', 'w')
computerHand.write('')
computerHand.close()
playerHand = open('playerhalfofdeck.txt', 'w')
playerHand.write('')
playerHand.close()

deck = open('Card.txt', 'r')
cards = deck.read()
cardOrder = cards.split(', ')
for i in range(52):
	if (i % 2) == 0:
		computerHand = open('computerhalfofdeck.txt', 'a')
		toWrite = cardOrder[i]
		toWrite += ', '
		computerHand.write(toWrite)
		computerHand.close()
	else:
		playerHand = open('playerhalfofdeck.txt', 'a')
		toWrite = cardOrder[i]
		toWrite += ', '
		playerHand.write(toWrite)
		playerHand.close()
