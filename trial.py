from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from os import urandom
import classpile
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = urandom(24)

@app.route('/', methods=['POST', 'GET'])
def index():
	#session['user'] = 'user'
	if request.method == 'POST':
		level = request.form['level']
		if level.lower() == 'easy':
			session['level'] = 'easy'
			session['newGame'] = True
			return redirect(url_for('easy'))
		elif level.lower() == 'hard':
			session['level'] = 'hard'
			session['newGame'] = True
			return redirect(url_for('hard'))
		else:
			error = "I don't understand, please try again"
			return render_template("index.html", error=error)
	else:
		return render_template("index.html")



@app.route('/easy', methods=['POST', 'GET'])
def easy():
	# Selecting word, specifying lives if new game
	if "newGame" in session and session['newGame'] == True:
		classpile.new_game(session, 7, "easy")
	# Guessing mechanism
	if request.method == 'POST':
		char = request.form['char']
		result = classpile.correct(char, session['wordSplit'])
		return classpile.guess(session, char, result)
	# If guess has not been made
	else:
		level = "easy"
		return render_template("guessing.html")

@app.route('/hard', methods=['POST', 'GET'])
def hard():
	# Selecting word, specifying lives if new game
	if "newGame" in session and session['newGame'] == True:
		classpile.new_game(session, 7, "hard")
		wordSplit = session['wordSplit']
	# Guessing mechanism
	if request.method == 'POST':
		char = request.form['char']
		result = classpile.correct(char, session['wordSplit'])
		return classpile.guess(session, char, result)
	# If guess has not been made
	else:
		session['level'] = "hard"
		return render_template("guessing.html")

@app.route('/test')
def test():
	return render_template("test.html")

if __name__ == "__main__":
	app.run()
