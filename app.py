from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import random 
import wordpile

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
	if request.method == "POST":
		level = request.form['level']
		if level == 'easy' or level == 'Easy':
			return redirect(url_for('testing')) # url_for links to the function that is called, not the url
			# return redirect('easy' is also valid, but then your website breaks if you change the url)
		elif level == 'hard' or level == 'Hard':
			return redirect(url_for('testing1'))
		else:
			error = "I don't understand, please try again"
			return render_template("index.html", error=error)
	else:
		return render_template("index.html")	

@app.route('/easy')
def testing():
	wordSplit = "ez"
	return render_template("guessing.html", wordSplit=wordSplit)

@app.route('/hard')
def testing1():
	wordSplit = "hz"
	return render_template("guessing.html", wordSplit=wordSplit)



if __name__ == "__main__":
	app.run()
