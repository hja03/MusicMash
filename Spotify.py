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