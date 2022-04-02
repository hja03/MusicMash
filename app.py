from flask import Flask, request, session, render_template, jsonify, url_for, flash
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"  # random secret key refreshes session variables on run
app.config['SESSION_TYPE']: 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_USE_SIGNER'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=2)
app.static_folder = 'static'

@app.route('/')
def hello_world():  # put application's code here
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
