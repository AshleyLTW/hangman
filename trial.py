from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from os import urandom
import classpile
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = urandom(24)

@app.route('/', methods=['POST', 'GET'])
def hangman_pic():
	pic = [
		"""
		
		""",
	    """
	    x-------x
	    """,
	    """
	    x-------x
	    |
	    |
	    |
	    |
	    |
	    """,
	    """
	    x-------x
	    |       |
	    |       0
	    |
	    |
	    |
	    """,
	    """
	    x-------x
	    |       |
	    |       0
	    |       |
	    |
	    |
	    """,
	    """
	    x-------x
	    |       |
	    |       0
	    |      /|\\
	    |
	    |
	    """,
	    """
	    x-------x
	    |       |
	    |       0
	    |      /|\\
	    |      /
	    |
	    """,
	    """
	    x-------x
	    |       |
	    |       0
	    |      /|\\
	    |      / \\
	    |
	    """
	]

	lives = 7

	return pic[7-lives]


if __name__ == "__main__":
	app.run()