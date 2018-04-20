from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from os import urandom
import classpile

app = Flask(__name__)
app.secret_key = urandom(24)

@app.route('/', methods=['POST', 'GET'])
def index():
	session['user'] = 'user'
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



@app.route('/easy')
def easy():
	if session['newGame'] == True:
		classpile.set_up(session, 10, "easy")
		return session['wordSplit']
	else:
		return "blurgh?"

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
