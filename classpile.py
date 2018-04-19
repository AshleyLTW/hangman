from flask import Flask
from flask import render_template
import random 
import wordpile


def selector(level):
	wordSplit = ""
	if level == "easy":
		wordNumber = random.randint(0, len(wordpile.wordsEasy)-1) 
		wordSelected = f"{wordpile.wordsEasy.pop(wordNumber)}"
		for character in wordSelected:
			wordSplit = wordSplit + character
		return wordSplit
	else: 
		wordNumber = random.randint(0, len(wordpile.wordsHard)-1) 
		wordSelected = f"{wordpile.wordsHard.pop(wordNumber)}"
		for character in wordSelected:
			wordSplit = wordSplit + character	
		return render_template("test.html", word=wordSplit)		


class player(object):
	def __init__(self, lives, level):
		self.lives = lives
		self.level = level

	def word(self):
		self.wordSplit = selector(self.level)
		return self.wordSplit

	def guess(self, char, wordSplit):
		if char in wordSplit:
			return "yes"
		else:
			return "no"

class build(object):
	def __init__(self, wordSplit):
		self.wordSplit = wordSplit

	def guess_space(self, wordSplit, guessed_letters):
		guess_space = ""
		for character in wordSplit:
			if character in guessed_letters:
				guess_space = guess_space + character + " "
			else:
				guess_space = guess_space + "_ "
		return guess_space
