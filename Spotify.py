from Track import Track
import requests


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
		print(self.tracks_str)
		r = requests.get('http://api.spotify.com/v1/audio-features', headers=self.headers,
						 params={'ids': self.tracks_str})
		print(r.json())
		i = 0
		self.track_objs = []
		for track in r.json()['audio_features']:
			track_obj = Track(track['danceability'], track['energy'], track['acousticness'], track['valence'],
						  track['tempo'], track['id'])
			i += 1
			self.track_objs.append(track_obj)
		return self.track_objs

#Get top 50 songs for a certain user
def getTop50(userID):

    ### Insert API jazz here ###
    trackIDs = getTrackIDsOfTop50(userID)
    tracks50 = getStatsOfAllTracks(trackIDs)

    return tracks50 #This should return a python list containing all of the track objects

def getTrackIDsOfTop50(userID):

    #Oh beautiful Matt do your thing

    return TracksID

def getStatsOfAllTracks(trackIds):

    return TrackObjects #List of track objects


# def getTrackAndStats(trackID):

#     return TrackObject