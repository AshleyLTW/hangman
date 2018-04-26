from nose.tools import *
from classpile import *
import wordpile 
from flask import Flask, session, request
from app import *
from unittest import mock
import unittest


wordsEasy = ["awkward", "bagpipes", "banjo", "crypt", "dwarves", "fishhook", "fjord", "gazebo", "haiku"]
wordsHard = ["abruptly", "askew", "boxcar", "disavow", "gizmo", "gnarly", "ivy", "ovary", "plegm", "thumbscrew"]


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



def test_newgame():
	with app.test_client() as c:
		app.secret_key = 'secret'
		with c.session_transaction() as sess:
			sess['guessed_letters'] = ["a"]
		rv = new_game(sess, 7, "easy")
		assert_false("guessed_letters" in sess)
		assert_true(sess.get('lives'))
		assert_true(sess.get('wordSplit'))

	



