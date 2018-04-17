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
		return render_template("test.html", word=wordSplit)
	else: 
		wordNumber = random.randint(0, len(wordpile.wordsHard)-1) 
		wordSelected = f"{wordpile.wordsHard.pop(wordNumber)}"
		for character in wordSelected:
			wordSplit.append(character)	
		return render_template("test.html", word=wordSplit)		
