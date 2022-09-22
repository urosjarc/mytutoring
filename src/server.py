from flask import Flask, request

from src import db

app = Flask(__name__)


@app.route("/test/<test_id>", methods=['POST', "GET"])
def test(test_id):
	exercise = db.exercises[test_id]
	if request.method == 'GET':
		return db.exercises[test_id].tests
	if request.method == 'POST':
		return request.json
