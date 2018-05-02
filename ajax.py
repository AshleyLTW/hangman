from flask import Flask, render_template, request, redirect, url_for, session, jsonify
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
			return redirect(url_for('easy'))
		elif level.lower() == 'hard':
			session['level'] = 'hard'
			return redirect(url_for('hard'))
		else:
			error = "I don't understand, please try again"
			return render_template("index.html", error=error)
	else:
		return render_template("index.html")



@app.route('/easy', methods=['POST', 'GET'])
def easy():
	# Selecting word, specifying lives 
	classpile.new_game(session, 7, "easy")
	return render_template("guessing.html")

@app.route('/_processing', methods=['POST', 'GET'])
def process():
	# Guessing mechanism
	char = request.args.get('char', type=str)
	result = classpile.correct(char, session['wordSplit'])
	return classpile.guess(session, char, result).

if __name__ == "__main__":
	app.run()