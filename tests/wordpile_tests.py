from nose.tools import *
from classpile import *
import wordpile
from flask import Flask, session
from app import *


wordsEasy = ["awkward", "bagpipes", "banjo", "crypt", "dwarves", "fishhook", "fjord", "gazebo", "haiku"]
wordsHard = ["abruptly", "askew", "boxcar", "disavow", "gizmo", "gnarly", "ivy", "ovary", "plegm", "thumbscrew"]
app = Flask(__name__)

def test_selectorEasy():
	assert_true(isinstance(selector("easy"), str))
	# not sure how to fix this since my function pops the word off of wordsEasy, should I just copy the string here and define it?
	assert_true(selector("easy")in wordsEasy)
	assert_false(selector("easy") in wordsHard)

def test_selectorHard():
	assert_true(isinstance(selector("hard"), str))
	# not sure how to fix this since my function pops the word off of wordsEasy, should I just copy the string here and define it?
	assert_true(selector("hard")in wordsHard)
	assert_false(selector("hard") in wordsEasy)


def test_charMatchedToWordSplit(): 
	char = "a"
	word = "apple"
	word2 = "forest"
	assert_equal("yes", correct(char, word))
	assert_equal("no", correct(char, word2))


def test_guessSpaceGeneration():
	wordSplit = "applesauce"
	guessed_letters = ['a', 'p','s']
	assert_equal("a p p _ _ s a _ _ _", space(wordSplit, guessed_letters))

# I'm doing something wrong below

# Is this the best way to test, I'm not sure if I tested more than what the scope of unit testing strictly is
# def test_newgame():
# 	with app.test_client() as c:
# 		app.secret_key = 'secret'
# 		with c.session_transaction() as sess:
# 			sess['newGame'] = True
# 			sess['guessed_letters'] = ["a"]
# 		rv = c.get('/easy')
# 		assert_equal(session.get('guessed_letters'), None)
# 		# Unsure about hardcoding in the 10 here
# 		assert_true(session.get('lives'))
# 		# Just checkign this one exists since I already verified the above function
# 		assert_true(session.get('wordSplit'))



