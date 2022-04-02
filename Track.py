from tempfile import TemporaryDirectory


class Track:
    def __init__(self, danceability, energy, acousticness, valence, tempo):
        self.danceability = danceability
        self.energy = energy
        self.acouticness = acousticness
        self.valence = valence
        self.tempo = tempo

    def compareSong(otherPersonsSongs):
        compatibility = 0 #0-100
        return compatibility

class top50Tracks:
    def __init__(self, listOfTop50Tracks):
        self.track = listOfTop50Tracks

    def compareAllTracks(self, otherUsersTop50):
        for track in self.tracks:
            track.compareSong()

    def compare1trackToAllSongs(self,track1):
        maxCompat = -1
        for track in self.tracks:
            compat = track1.compareSong(track)
            if compat > maxCompat:
                maxCompat = compat

        return maxCompat