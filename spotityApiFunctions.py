import Track

#Get top 50 songs for a certain user
def getTop50(userID):

    ### Insert API jazz here ###
    trackIDs = getTrackIDsOfTop50
    tracks50 = getStatsOfAllTracks(trackIDs)

    return tracks50 #This should return a python list containing all of the track objects

def getTrackIDsOfTop50():
    
    #Oh beautiful Matt do your thing

    return TracksID

def getStatsOfAllTracks(trackIds):

    return TrackObjects #List of track objects


# def getTrackAndStats(trackID):

#     return TrackObject