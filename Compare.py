import Spotify
from Track import Track
import math
import requests

# idk if this works yet
def comparisonScore(user1, user2):

	tracks1 = user1.top_50_tracks()
	tracks2 = user2.top_50_tracks()

	vector1 = [0,0,0,0,0]
	for track in tracks1:
		vector1[0] += track.acousticness
		vector1[1] += track.danceability
		vector1[2] += track.energy
		vector1[3] += track.tempo
		vector1[4] += track.valence
	vector1 = [x / len(tracks1) for x in vector1]

	vector2 = [0,0,0,0,0]
	for track in tracks2:
		vector2[0] += track.acousticness
		vector2[1] += track.danceability
		vector2[2] += track.energy
		vector2[3] += track.tempo
		vector2[4] += track.valence
	vector2 = [x / len(tracks2) for x in vector2]

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
		vector1[0].append(track.acousticness)
		vector1[1].append(track.danceability)
		vector1[2].append(track.energy)
		vector1[3].append(track.tempo)
		vector1[4].append(track.valence)

	vector2 = [[],[],[],[],[]]
	for track in tracks1:
		vector2[0].append(track.acousticness)
		vector2[1].append(track.danceability)
		vector2[2].append(track.energy)
		vector2[3].append(track.tempo)
		vector2[4].append(track.valence)

	stats = ["acousticness", "danceability", "energy", "tempo", "valence"]
	output = {}

	for index, stat in enumerate(stats):
		u1_min = min(vector1[index])
		u1_avg = sum(vector1[index]) / len(vector1)
		u1_max = max(vector1[index])

		u2_min = min(vector2[index])
		u2_avg = sum(vector2[index]) / len(vector2)
		u2_max = max(vector2[index])

		output["min_" + stat] = min(u1_min, u2_min)
		output["target_" + stat] = (u1_avg + u2_avg) / 2
		output["max_" + stat] = max(u1_max, u2_max)

	output["min_tempo"] = output["min_tempo"] * 200
	output["target_tempo"] = output["target_tempo"] * 200
	output["max_tempo"] = output["max_tempo"] * 200

	# now do top artists, songs and genres into the dict
	artists = []
	songs = []
	genres = []

	songs.append(tracks1[0].trackID)
	#songs.append(tracks1[1].trackID)
	#songs.append(tracks2[0].trackID)
	#songs.append(tracks2[1].trackID)

	u1artists = user1.get_top_x_artists(5)
	u2artists = user2.get_top_x_artists(5)

	u1genres = user1.get_top_genres()
	u2genres = user2.get_top_genres()

	genres.append(u1genres[0])
	#genres.append(u1genres[1])
	genres.append(u2genres[0])
	#genres.append(u2genres[1])


	artists.append(u1artists[0].id)
	#artists.append(u1artists[1].id)
	artists.append(u2artists[0].id)
	#artists.append(u2artists[1].id)

	output["seed_artists"] = ",".join(artists)
	output["seed_genres"] = ",".join(artists)
	output["seed_tracks"] = ",".join(songs)

	return output


def compareScoreV2(user1, user2):
	tracks1 = user1.top_50_tracks()
	tracks2 = user2.top_50_tracks()

	matching = []
	for t1 in tracks1:
		for t2 in tracks2:
			if t1.genre == t2.genre:
				matching.append(t1.compareSong(t2))

	proportion_matching = len(matching) / (len(tracks1)*len(tracks2))
	avg_distance = sum(matching)  / (len(tracks1)*len(tracks2))

	print("Proportion, avg dist: ", proportion_matching, avg_distance)
	return proportion_matching * avg_distance



def compareScoreV3(user1, user2):
	tracks1 = user1.top_50_tracks()
	tracks2 = user2.top_50_tracks()
	
	total_compats = []
	for t1 in tracks1:
		compats = []
		for t2 in tracks2:
			compats.append(t1.compareSong(t2))
		total_compats.append(max(compats))

	for t2 in tracks2:
		compats = []
		for t1 in tracks1:
			compats.append(t2.compareSong(t1))
		total_compats.append(max(compats))

	score = (sum(total_compats) / len(total_compats)) * 100
	score = (0.3633 * math.exp(1.341 * score)) - 0.3664
	return score

def sortTracksByCompat(tracks_json_in, user1, user2):
		tracks_json = tracks_json_in['tracks']

		ids = []
		for track in tracks_json:
			ids.append(track['id'])
		ids_str = ",".join(ids)
		r = requests.get('http://api.spotify.com/v1/audio-features', headers=user1.headers,
						 params={'ids': ids_str})

		track_objs = []
		for track in r.json()['audio_features']:
			track_obj = Track(track['danceability'], track['energy'], track['acousticness'], track['valence'],
						  track['tempo'], track['id'])
			track_objs.append(track_obj)


		tracks1 = user1.track_objs
		tracks2 = user2.track_objs

		vector1 = [0,0,0,0,0]
		for track in tracks1:
			vector1[0] += track.acousticness
			vector1[1] += track.danceability
			vector1[2] += track.energy
			vector1[3] += track.tempo
			vector1[4] += track.valence
		vector1 = [x / len(tracks1) for x in vector1]

		vector2 = [0,0,0,0,0]
		for track in tracks2:
			vector2[0] += track.acousticness
			vector2[1] += track.danceability
			vector2[2] += track.energy
			vector2[3] += track.tempo
			vector2[4] += track.valence
		vector2 = [x / len(tracks2) for x in vector2]

		u1vector = Track(vector1[0], vector1[1],vector1[2],vector1[3],vector1[4], -1)
		u2vector = Track(vector2[0], vector2[1],vector2[2],vector2[3],vector2[4], -1)

		compat_track_dict = {}
		for track in track_objs:
			track_compat = track.compareSong(u1vector) * track.compareSong(u2vector)
			compat_track_dict[track] = track_compat

		sorted_list = [k for k, v in sorted(compat_track_dict.items(), key=lambda item: item[1])]

		actual_json_data = []
		for track in sorted_list:
			for json_track in tracks_json:
				if track.trackID == json_track['id']:
					actual_json_data.append(json_track)

		return actual_json_data