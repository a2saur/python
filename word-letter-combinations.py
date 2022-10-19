import random


def string(myList):
	string = ""
	for letter in myList:
		string += letter
	return string


TRIES = 500

word = list(input("Word: "))
scramblings = []
for x in range(TRIES):
	random.shuffle(word)
	if string(word) not in scramblings:
		scramblings.append(string(word))

for x in sorted(scramblings):
	print(string(x))


