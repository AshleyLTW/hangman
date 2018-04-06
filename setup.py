try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Hello World'
	'author': 'Ashley',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['hangman'],
	'scripts': [],
	'name': 'Hello World'
}

setup(**config)