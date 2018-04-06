from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import classpile


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
	if request.method == "POST":
		level = request.form['level']
		if level == 'easy' or level == 'Easy':
			return redirect(url_for('easy')) # url_for links to the function that is called, not the url
			# return redirect('easy' is also valid, but then your website breaks if you change the url)
		elif level == 'hard' or level == 'Hard':
			return redirect(url_for('hard'))
		else:
			error = "I don't understand, please try again"
			return render_template("index.html", error=error)
	else:
		return render_template("index.html")	

@app.route('/easy')
def easy():
	classpile.selector()


@app.route('/hard')
def hard():
	return "pass"



if __name__ == "__main__":
	app.run()
