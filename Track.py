from tempfile import TemporaryDirectory
import math
import requests


class Track:
	def __init__(self, danceability, energy, acousticness, valence, tempo, trackID, genre=None, name=None, url=None):
		self.danceability = danceability
		self.energy = energy
		self.acousticness = acousticness
		self.valence = valence
		self.trackID = trackID
		# tempo starts in BPM / by 200 to standardise to roughly 0 - 1
		self.tempo = tempo / 200
		self.genre = genre
		self.name = name
		self.url = url

	def compareSong(self, otherPersonsSong):
		compatibility = 0  # 0-100

		# finds the distance between the two tracks so the closer to 0 the more compatable
		compatibility = math.sqrt((self.danceability - otherPersonsSong.danceability) ** 2
								  + (self.energy - otherPersonsSong.energy) ** 2
								  + (self.acousticness - otherPersonsSong.acousticness) ** 2
								  + (self.valence - otherPersonsSong.valence) ** 2
								  + (self.tempo - otherPersonsSong.tempo) ** 2)

		# not compatible 0 - 1 most compatable
		compatibility = 1 - compatibility

		# skews the number to be more representative of compatability
		#compatibility = 1 / (1 + math.exp(-10 * (compatibility - 0.3)))

		# make into percentage
		#compatibility *= 100

		return compatibility

	def printTracks(self):
		for danceability, energy, acousticne, valence, trackID in zip(self.danceability, self.energy, self.acousticness, self.valence, self.trackID):
			print("danceability: ", danceability, "Energy: ", energy, "acousticness: ",acousticne, "valence: ", valence, "trackID: ", trackID)

	def __eq__(self, other):
		return self.name == other.name

	def __hash__(self):
		return hash(self.name)


class top50Tracks:
	def __init__(self, listOfTop50Tracks):
		self.track = listOfTop50Tracks

	def compareAllTracks(self, otherUsersTop50):
		for track in self.tracks:
			track.compareSong()

	def compare1trackToAllSongs(self, track1):
		maxCompat = -1
		for track in self.tracks:
			compat = track1.compareSong(track)
			if compat > maxCompat:
				maxCompat = compat

			return maxCompat