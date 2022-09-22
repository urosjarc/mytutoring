from flask import Flask, request

from src import db

app = Flask(__name__)


@app.route("/test/<test_id>", methods=['POST', "GET"])
def test(test_id):
	exercise = db.exercises[test_id]
	if request.method == 'GET':
		return db.exercises[test_id]._inputs
	if request.method == 'POST':
		passing = True
		predicted = request.json
		expected = db.exercises[test_id]._outputs
		for i in range(len(predicted)):
			fail = predicted[i]['output'] != expected[i]
			if fail:
				passing = False
			predicted[i]['expected'] = expected[i]
			predicted[i]['pass'] = not fail
		print('PASS:', passing)
		return predicted
