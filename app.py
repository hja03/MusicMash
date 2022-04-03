import copy

from flask import Flask, request, session, render_template, jsonify, url_for, flash, redirect, Response
from datetime import timedelta
import hashlib
import requests
import base64

import Graph
import Compare
import Spotify

app = Flask(__name__)
app.config['SECRET_KEY'] = "secfrefdtsdedy"  # random secret key refreshes session variables on run
app.config['SESSION_TYPE']: 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_USE_SIGNER'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=2)
app.static_folder = 'static'


@app.route('/')
def hello_world():  # put application's code here
	return render_template("login.html")


@app.route('/spotify-auth')
def spotify_authorise():
	response = redirect('https://accounts.spotify.com/authorize?client_id=af9db20ad8e342afbb98888472777ded'
						'&response_type=code&redirect_uri=http://127.0.0.1:5000/spotify-callback&scope=user-read-private '
						'user-follow-read user-library-read playlist-read-private user-top-read user-read-recently-played '
						'playlist-modify-public playlist-modify-private'
						'&show_dialog=true')
	return response


@app.route('/spotify-callback')
def spotify_callback():
	r = requests.post(headers={'Authorization': f'Basic YWY5ZGIyMGFkOGUzNDJhZmJiOTg4ODg0NzI3NzdkZWQ6OTlhODRlNzMwMDg4NDcyY2EwMmYzZmM1NDI1NjJjNWU=',
							   'Content-Type': 'application/x-www-form-urlencoded'},
					  params={'grant_type': 'authorization_code', 'code': request.args.get('code'), 'redirect_uri': 'http://127.0.0.1:5000/spotify-callback'},
					  url='https://accounts.spotify.com/api/token')
	if 'access_token_1' not in session.keys():
		session['access_token_1'] = r.json()['access_token']
		return redirect('/?login=2')
	else:
		session['access_token_2'] = r.json()['access_token']
	return redirect('/result')

@app.route('/use-data')
def play():
	user1 = Spotify.Client(session['access_token_1'])
	user2 = Spotify.Client(session['access_token_2'])


	session.clear()
	return 

@app.route('/result')
def result():
	data = {}
	user1 = Spotify.Client(session['access_token_1'])
	user2 = Spotify.Client(session['access_token_2'])
	data['name'] = [user1.name, user2.name]
	data['top3'] = [user1.top_50_tracks(3), user2.top_50_tracks(3)]
	data['top_genre'] = [user1.get_top_genres()[0][0], user2.get_top_genres()[0][0]]

	user1.get_top_x_artists(50)
	top_genres1 = user1.get_top_genres()[1]
	user2.get_top_x_artists(50)
	top_genres2 = user2.get_top_genres()[1]
	print(top_genres1)
	print(top_genres2)
	process_genres1 = Compare.simplify_genres(top_genres1)
	process_genres2 = Compare.simplify_genres(top_genres2)
	print(Compare.compare_genre_score(process_genres1, process_genres2))

	data['top_tracks'] = [enumerate(user1.top_50_tracks(3), 1), enumerate(user2.top_50_tracks(3), 1)]
	data['usr_img'] = [user1.img, user2.img]
	# data['compatibility'] = round(Compare.comparisonScore(user1, user2))
	data['compatibility'] = Compare.compare_genre_score(process_genres1, process_genres2)
	tracks = user1.get_recommendations(params=Compare.comparisonStats(user1, user2))
	track_art = []
	for track in tracks['tracks']:
		track_art.append(track['album']['images'][0]['url'])
	data['track_art'] = track_art
	tracks = user1.get_recommendations(params=Compare.comparisonStats(user1, user2))['tracks']
	ids = []



	playlist = user1.create_playlist(f"{user1.name} and {user2.name} Fusion", "Hackathon test playlist")
	playlist2 = user2.create_playlist(f"{user1.name} and {user2.name} Fusion", "Hackathon test playlist")
	tracksdata = Compare.sortTracksByCompat(tracks, user1, user2)

	# user1.add_tracks_to_playlist(tracksdata, playlist)
	# user2.add_tracks_to_playlist(tracksdata, playlist2)



	# tracks = user1.top_50_tracks()
	session.clear()
	return render_template('home.html', data=data)

# @app.route('/write-playlist')
# def write_playlist():
#

if __name__ == '__main__':
	app.run()