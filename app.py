from flask import Flask
from flask import render_template
import random 
import wordpile

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def selector():
	wordNumber = random.randint(0, len(wordpile.words)-1) 
	wordSelected = wordpile.words.pop(wordNumber)
	return wordSelected



if __name__ == "__main__":
	app.run()
