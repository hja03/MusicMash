import Spotify
from Track import Track
import math

# idk if this works yet
def comparisonScore(user1, user2):

	tracks1 = user1.top_50_tracks()
	tracks2 = user2.top_50_tracks()

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

def comparisonStats(user1, user2):
	tracks1 = user1.top_50_tracks()
	tracks2 = user2.top_50_tracks()

	vector1 = [[],[],[],[],[]]
	for track in tracks1:
		vector1[0].append(track.acouticness)
		vector1[1].append(track.danceability)
		vector1[2].append(track.energy)
		vector1[3].append(track.tempo)
		vector1[4].append(track.valence)

	vector2 = [[],[],[],[],[]]
	for track in tracks1:
		vector2[0].append(track.acouticness)
		vector2[1].append(track.danceability)
		vector2[2].append(track.energy)
		vector2[3].append(track.tempo)
		vector2[4].append(track.valence)

	stats = ["acousticness", "danceability", "energy", "tempo", "valence"]
	output = {}

	for index, stat in enumerate(stats):
		u1_min = min(vector1[index])
		u1_avg = sum(vector1[index]) / 50
		u1_max = max(vector1[index])

		u2_min = min(vector2[index])
		u2_avg = sum(vector2[index]) / 50
		u2_max = max(vector2[index])

		output["min_" + stat] = min(u1_min, u2_min)
		output["target_" + stat] = (u1_avg + u2_avg) / 2
		output["max_" + stat] = max(u1_max, u2_max)

	output["min_tempo"] = output["min_tempo"] * 200
	output["target_tempo"] = output["target_tempo"] * 200
	output["max_tempo"] = output["max_tempo"] * 200

	return output