from flask import Flask
import random 
import wordpile


def selector(self, foo):
	self.foo = level
	wordSplit = []
	if self.foo == "easy":
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
