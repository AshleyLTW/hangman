from flask import Flask
from flask import render_template
import random 
import wordpile


def selector(level):
	wordSplit = []
	if level == "easy":
		wordNumber = random.randint(0, len(wordpile.wordsEasy)-1) 
		wordSelected = f"{wordpile.wordsEasy.pop(wordNumber)}"
		for character in wordSelected:
			wordSplit.append(character)
		return wordSplit
	else: 
		wordNumber = random.randint(0, len(wordpile.wordsHard)-1) 
		wordSelected = f"{wordpile.wordsHard.pop(wordNumber)}"
		for character in wordSelected:
			wordSplit.append(character)	
		return render_template("test.html", word=wordSplit)		


class player(object):
	def __init__(self, lives, level):
		self.lives = lives
		self.wordSplit = selector(level)

	def lose_life(self):
		self.lives -= 1
		return self.lives

	def guess(self, char):
		if char in self.wordSplit:
			return "yes"
		else:
			return "no"

	def word(self):
		return self.wordSplit

