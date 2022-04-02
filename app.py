from flask import Flask, request, session, render_template, jsonify, url_for, flash, redirect, Response
from datetime import timedelta
import hashlib
import requests
import base64

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


@app.route('/spotify-auth')
def spotify_authorise():
	response = redirect('https://accounts.spotify.com/authorize?client_id=af9db20ad8e342afbb98888472777ded'
						'&response_type=code&redirect_uri=http://127.0.0.1:5000/spotify-callback')
	return response


@app.route('/spotify-callback')
def spotify_callback():
	r = requests.post(headers={'Authorization': f'Basic YWY5ZGIyMGFkOGUzNDJhZmJiOTg4ODg0NzI3NzdkZWQ6OTlhODRlNzMwMDg4NDcyY2EwMmYzZmM1NDI1NjJjNWU=',
							   'Content-Type': 'application/x-www-form-urlencoded'},
					  params={'grant_type': 'authorization_code', 'code': request.args.get('code'), 'redirect_uri': 'http://127.0.0.1:5000/spotify-callback'},
					  url='https://accounts.spotify.com/api/token')
	session['access_token'] = r.json()['access_token']

	return session.get('access_token')



if __name__ == '__main__':
	app.run()
