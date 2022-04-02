import Spotify
from Track import Track
import math

# idk if this works yet
def comparisonScore(user1, user2):
	client1 = user1
	client2 = user2

	tracks1 = client1.top_50_tracks()
	tracks2 = client2.top_50_tracks()

	vector1 = [0,0,0,0,0]
	for track in tracks1:
		vector1[0] += track.acouticness
		vector1[1] += track.danceability
		vector1[2] += track.energy
		vector1[3] += track.tempo
		vector1[4] += track.valence
	vector1 = [x / 50 for x in vector1]

	vector2 = [0,0,0,0,0]
	for track in tracks2:
		vector2[0] += track.acouticness
		vector2[1] += track.danceability
		vector2[2] += track.energy
		vector2[3] += track.tempo
		vector2[4] += track.valence
	vector2 = [x / 50 for x in vector2]

	compatability = 0
	for i in range(5):
		compatability += (vector1[i] - vector2[i]) ** 2
	compatability = math.sqrt(compatability)

	compatability = 1 - compatability
	#compatability = 1 / (1 + math.exp(-10 * (compatability - 0.3)))
	compatability *= 100


	return compatability

