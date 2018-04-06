try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Your basic hangman game'
	'author': 'Ashley',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'my email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['hangman'],
	'scripts': [],
	'name': 'Hangman'
}

setup(**config)