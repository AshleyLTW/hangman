class Pregame(object):
	def selector():
		wordSplit = []
		wordNumber = random.randint(0, len(wordpile.words)-1) 
		wordSelected = f"{wordpile.words.pop(wordNumber)}"
		for character in wordSelected:
			wordSplit.append(character)
		return render_template("index.html", wordSplit=wordSplit)	


class Pregame(object):
	def __init__(self, level):
		self.level = level

	def selector(self):
		wordSplit = []
		if self.level == "easy":
			wordNumber = random.randint(0, len(wordpile.wordsEasy)-1) 
			wordSelected = f"{wordpile.wordsEasy.pop(wordNumber)}"
			for character in wordSelected:
				wordSplit.append(character)
			return render_template("test.html", word=wordSplit)
		else: 
			wordNumber = random.randint(0, len(wordpile.wordsHard)-1) 
			wordSelected = f"{wordpile.wordsHard.pop(wordNumber)}"
			for character in wordSelected:
				wordSplit.append(character)			


--------

import random 

class Pregame(object):
	def __init__(self, level):
		self.level = level

	def selector(self, level):
		self.wordSplit = []
		wordBank = "wordpile.words" + self.level
		self.wordNumber = random.randint(0, len(wordBank)-1) 
		self.wordSelected = f"{wordBank.pop(wordNumber)}"
		for character in wordSelected:
			wordSplit.append(character)			