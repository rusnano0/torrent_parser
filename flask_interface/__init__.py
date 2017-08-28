from flask import Flask, render_template, url_for, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient()
db = client.torrent_parser
books = db.books

@app.route('/', methods=['POST', 'GET'])
def index():
	""" Index page """
	return render_template('index.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
	"""search page"""
	if request.method == "GET":
		userquery = request.args.get('q', '')
		result = [i for i in books.find({'$text': {'$search': userquery} },{'score': { '$meta': "textScore" } }).sort([('score', {'$meta': 'textScore'})]) ]

	return render_template('search.html', userquery=userquery, result=result)


if __name__ == "__main__":
	app.run(debug=True)


