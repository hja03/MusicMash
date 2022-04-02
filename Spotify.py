import Track
import requests


class Client:
	def __init__(self, access_token):
		self.access_token = access_token

	def top_50_tracks(self):
		r = requests.get('https://api.spotify.com/v1/me/top/tracks', headers= {'Authorization': f'Bearer {self.access_token}'},
						 params={'limit': 50})
		self.tracks = []
		for i in r.json()["items"]:
			# self.tracks += (i["track"]["uri"] + ",")
			self.tracks.append(i['id'])
		# self.tracks = self.tracks[:-1]
		# print(self.tracks)
		return self.tracks