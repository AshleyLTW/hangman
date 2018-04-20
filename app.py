from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from os import urandom
import classpile

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
			return redirect(url_for('hard'))
		else:
			error = "I don't understand, please try again"
			return render_template("index.html", error=error)
	else:
		return render_template("index.html")



@app.route('/easy', methods=['POST', 'GET'])
def easy():
	# session['newGame'] = True # Temporary to save me some time
	# Selecting word, specifying lives if new game
	if "newGame" in session and session['newGame'] == True:
		classpile.new_game(session, 10, "easy")
	# Guessing mechanism
	if request.method == 'POST':
		# Check player is still alive
		if session['lives'] > 0: 
			char = request.form['char']
			result = classpile.correct(char, session['wordSplit'])
			return classpile.guess(session, char, result)
		# If player is dead
		else: 
			return render_template("death.html", wordSplit=session['wordSplit'])
	# If guess has not been made
	else:
		return render_template("guessing.html")

@app.route('/hard', methods=['POST', 'GET'])
def hard():
	return classpile.selector("hard")


if __name__ == "__main__":
	app.run()
