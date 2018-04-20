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
		if level == 'easy' or 'Easy':
			session['level'] = 'easy'
			session['newGame'] = True
			return redirect(url_for('easy'))
		elif level == 'hard' or 'Hard':
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
	if session['newGame'] == True:
		classpile.new_game(session, 10, "easy")
	# Guessing mechanism
	if request.method == 'POST':
		# Check player is still alive
		if session['lives'] > 0: 
			char = request.form['char']
			result = classpile.guess(char, session['wordSplit'])
			session['newGame'] = False 
			# If guess is a new character, add guess to guessed letters
			if session.get('guessed_letters') == True and char not in session['guessed_letters']:
				session['guessed_letters'].append(char)
			guess_space = classpile.guess_space(session['wordSplit'], session['guessed_letters'], session)
			# If guess has been made before
			if session.get('guessed_letters') == True and char in session['guessed_letters']:
				warning = "This letter has been guessed before! Please choose another one!"
				return render_template('guessing.html', lives=session['lives'], warning=warning, guess_space=guess_space, wordSplit = session['wordSplit'], guessed_letters=session['guessed_letters'])			
			# If guess is correct
			if result == 'yes':
				return render_template('guessing.html', lives=session['lives'], guess_space=guess_space, wordSplit = session['wordSplit'], guessed_letters=session['guessed_letters'])
			# Subtract life for incorrect guess
			else:
				session['lives'] = session['lives'] - 1
				return render_template('guessing.html', lives=session['lives'], guess_space=guess_space, wordSplit = session['wordSplit'], guessed_letters=session['guessed_letters'])
		# If player is dead
		else: 
			return render_template("death.html", wordSplit=session['wordSplit'])
	# If guess has not been made
	else:
		return render_template("guessing.html")

@app.route('/hard', methods=['POST', 'GET'])
def hard():
	return classpile.selector("hard")

@app.route('/getsession')
def getsession():
	if 'user' in session:
		classpile.test(session)
		return session['foo']
	else:
		return "Not logged in!"

if __name__ == "__main__":
	app.run()
