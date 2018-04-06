from flask import Flask
from flask import render_template
import random 
import wordlist

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def selector():
	wordNumber = random.randint(0, len(wordlist.words)-1) 
	return wordlist.words[wordNumber]

if __name__ == "__main__":
	app.run()
