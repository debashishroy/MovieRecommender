import numpy as np

    
def getUserMappingID(userIdOriginal):
    fileUsers = open('users.txt','r')
    for row in fileUsers:
        splitRow = row.split(",")
        mapid = splitRow[0].strip()
        originalIDFile= splitRow[1].strip()
        if userIdOriginal == originalIDFile:
            fileUsers.close()
            return mapid
    fileUsers.close()

def getMovieMappingID(movieIdOriginal):
    fileMovies = open('movies.txt','r')
    for row in fileMovies:
        splitRow = row.split(",")
        mapid = splitRow[0].strip()
        originalIDFile= splitRow[1].strip()
        if movieIdOriginal == originalIDFile:
            fileMovies.close()
            return mapid
    fileMovies.close()

matrixSize= (1000,1000)
ratingMatrix= np.zeros(matrixSize)
flRatingsFile = open('nfRatings.txt','r')
k=1
for row in flRatingsFile:
    splitRow = row.split(",")
    print(k,":",row.strip())
    k=k+1
    userid= splitRow[0]
    movieID=splitRow[1]
    rating = splitRow[2]
    uid = getUserMappingID(userid)
    mid= getMovieMappingID(movieID)
    u=int(uid)
    m=int(mid)
    ratingMatrix[u][m]=float(rating)

np.savetxt('nflxRatingMatrix.txt',ratingMatrix,fmt='%.4f')


flRatingsFile.close()

    


