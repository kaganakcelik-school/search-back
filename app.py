from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return "this is a rly cool home page"

@app.route('/api/search/<search>')
def get_user(search):
	question = search

	try: 
			from googlesearch import search 
	except ImportError:  
			print("No module named 'google' found") 

	# to search 
	query = question

	searchItems = []
	searchDictionary = {}


	for j in search(question, num=10, stop=10, pause=2): 
		searchItems.append(j)


	for i in range(len(searchItems)):
		searchDictionary[i] = searchItems[i]

	return jsonify(searchDictionary), 200




if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0')