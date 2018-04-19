# A functioning hangman program except that I can't get it to work with Flask
player = classpile.player(10, "easy")
secret = player.wordSplit
guess = request.form['char']
remaining_letters = len(secret)
guess_space = []

while player.lives > 0 and remaining_letters > 0:
	for character in secret:
		if character in guessed_letters:
			guess_space.append(character)
		else: 
			guess_space.append(_)


	return render_template("test.html", lives=player.lives, guess_space=guess_space)	














@app.route('/easy', methods=['POST', 'GET'])
def easy():
	if request.method =="POST":
		wordSplit=classpile.selector("easy")
		char = request.form['char']
		result = classpile.guess(char, wordSplit)
		return render_template("guessing.html", wordSplit=wordSplit, result=result)
	else:
		return render_template("guessing.html")

----
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