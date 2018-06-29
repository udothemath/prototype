# // ./app.py
from flask import Flask

app = Flask(__name__)

@app.route('/',  methods=['POST'])
def index():
	return "Yo, it's working!"

if __name__ == "__main__":
	app.run()