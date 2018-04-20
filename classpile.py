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
		return ''.join(wordSplit)
	else: 
		wordNumber = random.randint(0, len(wordpile.wordsHard)-1) 
		wordSelected = f"{wordpile.wordsHard.pop(wordNumber)}"
		for character in wordSelected:
			wordSplit.append(character)	
		return ''.join(wordSplit)


def correct(char, wordSplit):
	if char in wordSplit:
		return "yes"
	else:
		return "no"

def space(wordSplit, guessed_letters, session):
	space = []
	for character in wordSplit:
		if character in session['guessed_letters']:
			space.append(character)
		else:
			space.append("_")
	return ' '.join(space)	

def new_game(session, lives, level): # Level must be a string
	session['wordSplit'] = selector(level)
	session['lives'] = lives
	session.pop('guessed_letters', None)


def guess(session, char, result):
	if "guessed_letters" not in session:
		session['guessed_letters'] = []
	session['newGame'] = False
	if char in session['guessed_letters']:
		warning = "This letter has been guessed before! Please choose another letter"
		guess_space = space(session['wordSplit'], session['guessed_letters'], session)
		return render_template('guessing.html', lives=session['lives'], warning=warning, guess_space=guess_space, guessed_letters=session['guessed_letters'])
	else:
		session['guessed_letters'].append(char)
		guess_space = space(session['wordSplit'], session['guessed_letters'], session)
		if result == 'yes':
			if "_" in guess_space:
				return render_template('guessing.html', lives=session['lives'], guess_space=guess_space, guessed_letters=session['guessed_letters'])
			else:
				wordSplit = session['wordSplit']
				return render_template('win.html', wordSplit=wordSplit)
		else: 
			session['lives'] = session['lives'] - 1
			if session['lives'] == 0: 
				return render_template("death.html", wordSplit=session['wordSplit'])
			else: 
				return render_template('guessing.html', lives=session['lives'], guess_space=guess_space, guessed_letters=session['guessed_letters'])













