import itertools

from Track import Track
import requests
from Artist import Artist

class Client:
	def __init__(self, access_token):
		self.access_token = access_token
		self.headers = {'Authorization': f'Bearer {self.access_token}', 'Content-Type': 'application/json'}
		r = requests.get('https://api.spotify.com/v1/me', headers=self.headers)
		self.name = r.json()['display_name']
		self.img = r.json()['images']
		if self.img:
			self.img = self.img[0]['url']
		else:
			self.img = 'https://icon-library.com/images/default-profile-icon/default-profile-icon-24.jpg'
		print(self.img)

	def top_50_tracks(self, limit=50):
		r = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=self.headers,
						 params={'limit': limit})
		self.tracks = []
		self.track_names = []
		for i in r.json()["items"]:
			self.tracks.append(i['id'])
			self.track_names.append(i['name'])
		self.tracks_str = ",".join(self.tracks)
		r = requests.get('http://api.spotify.com/v1/audio-features', headers=self.headers,
						 params={'ids': self.tracks_str})
		i = 0
		self.track_objs = []
		for track, track_name in zip(r.json()['audio_features'], self.track_names):
			track_obj = Track(track['danceability'], track['energy'], track['acousticness'], track['valence'],
							  track['tempo'], track['id'], name=track_name)
			self.track_objs.append(track_obj)
		return self.track_objs

	def get_top_x_artists(self, limit):
		r = requests.get('https://api.spotify.com/v1/me/top/artists', headers=self.headers,
						 params={'limit': limit})
		self.artists = []
		print(r.json())
		for artist in r.json()['items']:
			artist_obj = Artist(artist['id'], artist['name'], artist['genres'], artist['popularity'])
			self.artists.append(artist_obj)
		return self.artists

	def get_top_genres(self, num=50):
		self.get_top_x_artists(num)
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

		for genre in sorted_genres.keys():
			genres.append(genre)
		return genres

	def get_recommendations(self, params):
		params = params
		params['limit'] = 50
		r = requests.get('https://api.spotify.com/v1/recommendations', headers=self.headers, params=params)
		return r.json()


	def get_current_user_profile(self):
		r = requests.get('https://api.spotify.com/v1/me', headers=self.headers)
		return r.json()

	def create_playlist(self, name, description):
		params = {'name':name, 'description':description}
		user_id = get_current_user_profile()['id']
		r = requests.post(f"https://api.spotify.com/v1/users/{user_id}/playlists", headers=self.headers, params=params)