import plotly.express as px
import pandas as pd

def graph(tracks):
	vector1 = [[],[],[],[],[]]
	for track in tracks:
		vector1[0].append(track.acousticness)
		vector1[1].append(track.danceability)
		vector1[2].append(track.energy)
		vector1[3].append(track.tempo)
		vector1[4].append(track.valence)

	df = pd.DataFrame(dict(acousticness=vector1[0], danceability=vector1[1], energy=vector1[2], tempo=vector1[3], valence=vector1[4]))
	fig = px.scatter_3d(df, x='acousticness', y='danceability', z='energy', color='tempo', size='valence')
	fig.show()