flRating = open('netflixRating.txt','r')
movieID=[]
AllUsers=[]
ratings=[]
for row in flRating:
    row = row.strip()
    splitRow= row.split(",")
    movieID.append(splitRow[0])
    AllUsers.append(splitRow[1])
    ratings.append(splitRow[2])
flRating.close()
print("Reading done")

freqUsers=[]
flFrequentUsers= open('frequentUsers.txt','r')
for row in flFrequentUsers:
    row=row.strip()
    splitRow= row.split(",")
    freqUsers.append(splitRow[0])
flFrequentUsers.close()

tempMovies=[]
for fqUser in freqUsers:
    nfScannedRatings=open('nfScannedRatings','a')
    indices = [i for i, x in enumerate(AllUsers) if x == fqUser]
    for i in indices:
        print ("{},{},{}".format(AllUsers[i],movieID[i],ratings[i]),file=nfScannedRatings)
        tempMovies.append(movieID[i])
    nfScannedRatings.close()

setMovies= set(movieID)
tempList= list(setMovies)
results = list(map(int, tempList))

results.sort()
for i in results:
    print (i)
