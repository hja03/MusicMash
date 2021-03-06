import Spotify
from Track import Track
import math
import requests
import copy

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
	vector1 = [x / 50 for x in vector1]

	vector2 = [0,0,0,0,0]
	for track in tracks2:
		vector2[0] += track.acousticness
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
	#compatability =  math.sin((math.pi / 2) * (compatability-1)) + 1
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
		u1_avg = sum(vector1[index]) / 50
		u1_max = max(vector1[index])

		u2_min = min(vector2[index])
		u2_avg = sum(vector2[index]) / 50
		u2_max = max(vector2[index])

		output["target_" + stat] = (u1_avg + u2_avg) / 2
		output["min_" + stat] = (min(u1_min, u2_min) + ((u1_avg + u2_avg) / 2)) / 2
		output["max_" + stat] = (max(u1_max, u2_max) + ((u1_avg + u2_avg) / 2)) / 2

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

	genres.append(u1genres[0][0])
	#genres.append(u1genres[1])
	genres.append(u2genres[0][0])
	#genres.append(u2genres[1])


	artists.append(u1artists[0].id)
	#artists.append(u1artists[1].id)
	artists.append(u2artists[0].id)
	#artists.append(u2artists[1].id)

	output["seed_artists"] = ",".join(artists)
	output["seed_genres"] = ",".join(genres)
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

	proportion_matching = len(matching) / (50**2)
	avg_distance = sum(matching)  / (50**2)

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

	return (sum(total_compats) / len(total_compats)) * 100

def sortTracksByCompat(tracks_json_in, user1, user2):
		tracks_json = tracks_json_in

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
		for json, track in zip(tracks_json, track_objs):
			track_compat = track.compareSong(u1vector) * track.compareSong(u2vector)
			compat_track_dict[track_compat] = json

		sorted_list = [v for k, v in sorted(compat_track_dict.items(), key=lambda item: item[0])]



		return sorted_list

def simplify_genres(genres):
	simplified = ['pop', 'indie', 'jazz', 'rock', 'funk', 'jazz', 'dance', 'metal']
	new_genres = copy.deepcopy(genres)
	for genre in genres.keys():
		for sub_genre in simplified:
			if sub_genre in genre:
				if sub_genre + '_add' in new_genres.keys():
					new_genres[sub_genre + '_add'] += genres[genre] * 2
				else:
					new_genres[sub_genre + '_add'] = genres[genre] * 2
	total_len = 0
	for val in new_genres.values():
		total_len += val
	return new_genres

def compare_genre_score(g1, g2):
	genres_len = len(g1.keys())
	genres_len += len(g2.keys())
	
	g1_total = 0
	g2_total = 0
	compatibility = 0
	for num in g1.values():
		g1_total += num
	for num in g2.values():
		g2_total += num
	total_total = g1_total + g2_total
	for key in g1.keys():
		if key in g2.keys():
			compatibility += min((g1[key] / g1_total), (g2[key] / g2_total))
			#compatibility += (g1[key] / g1_total) / (g1_total / g2_total)
			#compatibility += (g2[key] / g2_total) / (g1_total / g2_total)
	# compatibility /= 1/total_total
	#compatibility *= 50
	compatibility *= 100
	return compatibility




def get_attributes(user):
	tracks1 = user.track_objs
	vector1 = [0,0,0,0,0]
	for track in tracks1:
		vector1[0] += track.acousticness
		vector1[1] += track.danceability
		vector1[2] += track.energy
		vector1[3] += track.tempo
		vector1[4] += track.valence
	vector1 = [(x / len(tracks1)) * 100 for x in vector1]
	return vector1

