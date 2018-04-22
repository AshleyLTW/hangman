from flask import Flask
from flask import render_template
import random 
import wordpile

# Choosing the word to be guessed
def selector(level):
	wordSplit = []
	if level == "easy":
		wordNumber = random.randint(0, len(wordpile.wordsEasy)-1) 
		wordSplit = f"{wordpile.wordsEasy.pop(wordNumber)}"
		return wordSplit
	else: 
		wordNumber = random.randint(0, len(wordpile.wordsHard)-1) 
		wordSplit = f"{wordpile.wordsHard.pop(wordNumber)}"
		return wordSplit

# Checking if the guess is correct
def correct(char, wordSplit):
	if char in wordSplit:
		return "yes"
	else:
		return "no"

# Creating the word that users will see (underscores if character is unguessed)
def space(wordSplit, guessed_letters):
	space = []
	for character in wordSplit:
		if character in guessed_letters:
			space.append(character)
		else:
			space.append("_")
	return ' '.join(space)	

# Setting up a new game
def new_game(session, lives, level): # Level must be a string
	session['wordSplit'] = selector(level)
	session['lives'] = lives
	session.pop('guessed_letters', None)

# Processing guess: checking if in/adding to already guessed list, subtracting lives, checking if still alive
def guess(session, char, result):
	if "guessed_letters" not in session:
		session['guessed_letters'] = []
	session['newGame'] = False
	if char in session['guessed_letters']:
		warning = "This letter has been guessed before! Please choose another letter"
		guess_space = space(session['wordSplit'], session['guessed_letters'])
		return render_template('guessing.html', lives=session['lives'], warning=warning, guess_space=guess_space, guessed_letters=session['guessed_letters'])
	else:
		session['guessed_letters'].append(char)
		guess_space = space(session['wordSplit'], session['guessed_letters'])
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













