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


def guess(char, wordSplit):
	if char in wordSplit:
		return "yes"
	else:
		return "no"

def guess_space(wordSplit, guessed_letters, session):
	guess_space = []
	for character in wordSplit:
		if session.get('guessed_letters') == True and character in session['guessed_letters']:
			guess_space.append(character)
		else:
			guess_space.append("_")
	return ' '.join(guess_space)	

def new_game(session, lives, level): # Level must be a string
	session['wordSplit'] = selector(level)
	session['guessed_letters'] = none
	session['lives'] = lives








