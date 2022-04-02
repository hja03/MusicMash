import itertools

from Track import Track
import requests
from Artist import Artist

class Client:
	def __init__(self, access_token):
		self.access_token = access_token
		self.headers = {'Authorization': f'Bearer {self.access_token}', 'Content-Type': 'application/json'}

	def top_50_tracks(self):
		r = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=self.headers,
						 params={'limit': 50})
		self.tracks = []
		for i in r.json()["items"]:
			self.tracks.append(i['id'])
		self.tracks_str = ",".join(self.tracks)
		r = requests.get('http://api.spotify.com/v1/audio-features', headers=self.headers,
						 params={'ids': self.tracks_str})
		i = 0
		self.track_objs = []
		for track in r.json()['audio_features']:
			track_obj = Track(track['danceability'], track['energy'], track['acousticness'], track['valence'],
						  track['tempo'], track['id'])
			i += 1
			self.track_objs.append(track_obj)
		return self.track_objs

	def get_top_x_artists(self, limit):
		r = requests.get('https://api.spotify.com/v1/me/top/artists', headers=self.headers,
						 params={'limit': limit})
		self.artists = []
		for artist in r.json()['items']:
			artist_obj = Artist(artist['id'], artist['name'], artist['genres'], artist['popularity'])
			self.artists.append(artist_obj)
		return self.artists

	def get_top_genres(self):
		genres = {}
		if self.artists:
			for artist in self.artists:
				for genre in artist.genre:
					if genre in genres.keys():
						genres[genre] += 1
					else:
						genres[genre] = 1
		sorted_genres_vals = sorted(genres.values())  # Sort the values
		sorted_genres = {}
		for i in sorted_genres_vals[::-1]:
			for k in genres.keys():
				if genres[k] == i:
					sorted_genres[k] = genres[k]
					break
		genres = []

		for genre in dict(itertools.islice(sorted_genres.items(), 5)).keys():
			genres.append(genre)
		return genres