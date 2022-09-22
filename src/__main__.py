from src import db
from src.server import app

if __name__ == '__main__':
	db.init()
	app.run(debug=True)
