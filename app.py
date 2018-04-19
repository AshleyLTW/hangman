from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect, url_for
import classpile


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
	if request.method == "POST":
		level = request.form['level']
		if level == 'easy' or level == 'Easy':
			resp = make_response(redirect(url_for('easy')))
			resp.set_cookie('newGame', "True")
			return resp # url_for links to the function that is called, not the url
			# return redirect('easy' is also valid, but then your website breaks if you change the url)
		elif level == 'hard' or level == 'Hard':
			return redirect(url_for('hard'))
		else:
			error = "I don't understand, please try again"
			return render_template("index.html", error=error)
	else:
		return render_template("index.html")	

@app.route('/easy', methods=['POST', 'GET'])

def easy():
	newGame = request.cookies.get('newGame')
	# Setting up lives and word to guess if it's a new game
	if newGame == "True":
		player = classpile.player(10, "easy")
		wordSplit = player.word()
		wordSplit = str(wordSplit)
		lives = player.lives
		resp = make_response(render_template('guessing.html', wordSplit = wordSplit, lives = lives))
		resp.set_cookie('wordSplit', wordSplit)
	# Establishing instance of player class if it isn't a new game
	else: 
		wordSplit = request.cookies.get('wordSplit')
		lives = request.cookies.get('lives')
		resp = make_response(render_template('guessing.html', wordSplit = wordSplit, lives = lives))
		player = classpile.player(request.cookies.get('lives'), "easy")
	# Guessing mechanism
	if request.method == "POST":
		# Checking player is still alive
		lives = int(lives)
		if lives > 1: 
			char = request.form['char']
			result = player.guess(char, wordSplit)
			resp.set_cookie('newGame', "False")
			lives = str(lives)
			# If guess is correct
			if result == "yes":
				resp.set_cookie('lives', lives)
				return resp
			# If guess is incorrect
			else: 
				lives = int(lives) 
				lives -= 1
				lives = str(lives)
				resp.set_cookie('lives', lives)
				return resp
		# If player is dead
		else:
			return render_template("death.html", wordSplit = wordSplit)

	# If guess has not been made
	else:
		return render_template("guessing.html")


@app.route('/hard', methods=['POST', 'GET'])
def hard():
	return classpile.selector("hard")



if __name__ == "__main__":
	app.run()
