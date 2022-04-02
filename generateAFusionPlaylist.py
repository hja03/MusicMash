def most_compatible_tracks(user1Top50,user2Top50):
    minCompat=90
    tracksInPlaylist = []

    for track in user1Top50:
        compat = user2Top50.compare1TrackToAllSongs(track)
        if compat > minCompat:
            tracksInPlaylist.append(track)
        
    return tracksInPlaylist
    