from flask import Flask
from flask import render_template
import random 
import wordpile

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def selector():
	wordSplit = []
	wordNumber = random.randint(0, len(wordpile.words)-1) 
	wordSelected = f"{wordpile.words.pop(wordNumber)}"
	for character in wordSelected:
		wordSplit.append(character)
	return render_template("index.html", wordSplit=wordSplit)



if __name__ == "__main__":
	app.run()
