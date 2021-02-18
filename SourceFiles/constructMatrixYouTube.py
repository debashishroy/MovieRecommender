import numpy as np
f = open('YouTubeRatings.txt','r')
users=[]
movies=[]
ratings=[]
for line in f:
    line=line.strip()
    ls=line.split(',')
    users.append(ls[0])
    movies.append(ls[1])
    ratings.append(ls[2])
f.close()

totUsers= len(set(users))
totMovies=len(set(movies))
print(totUsers,totMovies)
matrixSize= (totUsers,totMovies)
ratingMatrix=np.zeros(matrixSize)
mrating=0
for mi in range (0,len(users)):
    uindex= int(users[mi])
    mindex = int(movies[mi])
    try:
        mrating= float(ratings[mi])
    except ValueError:
        #print(mrating)
        mrating=0
    if uindex<totUsers and mindex<1000:
        ratingMatrix[uindex][mindex]=mrating
nonZero=0
for k in range(0,3):
    #print(len(ratingMatrix),len(ratingMatrix[0]))
    for u in range(0, len(ratingMatrix)):
        zeroCount=0
        for m in range(0, len(ratingMatrix[0])):
            if ratingMatrix[u][m]==0.0:
                zeroCount=zeroCount+1
        if zeroCount==1000:
            ratingMatrix=np.delete(ratingMatrix,u,axis=0)
            break

    
#print(zeroCount)

print(len(ratingMatrix),len(ratingMatrix[0]))         
    
'''
for i in range(ratingMatrix[0]):
    for j in range(0,)
'''
    
np.savetxt('youTubeRatingMatrix2.txt',ratingMatrix,fmt='%.2f')
    
    
    




    
