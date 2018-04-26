import unittest
from app import app
import classpile
from nose.tools import *
from flask import Flask, session
import pprint
class HangmanTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		pass

class newGame(HangmanTest):
	def newGame(self, session, lives, level):
		return self.app.get('/easy', data=dict(
			session=session,
			lives=lives,
			level=level
		), follow_redirects = True)
	def test_newGame(self):
		with app.test_client() as c:
			app.secret_key = 'secret'
			
			with c.session_transaction() as sess:
				sess['newGame'] = True
				sess['guessed_letters'] = ["a"]
				# pprint.pprint(sess)
				# pprint.pprint(session)
			rv = classpile.new_game(sess, 7, 'easy')
			# pprint.pprint(sess)
			# pprint.pprint(session)
			assert_false("guessed_letters" in sess) 
			# pprint.pprint(sess)
				# pprint.pprint(session)
