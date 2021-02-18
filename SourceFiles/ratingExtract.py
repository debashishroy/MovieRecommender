mvRat = open("ratings.csv",'r')
mapfile= open("mappedID.txt",'r')
scannedRatings=open("scannedRatings.txt",'w')

movielensId=[]
for line in mapfile:
    line=line.strip()
    splitLine= line.split(',')
    movielensId.append(splitLine[1].strip())
'''
k=movielensId.index("7149")
print(k)
'''
foundMovies=[]
b=0
counter=0
for line in mvRat:
    line=line.strip()
    if counter>0:
        sl= line.split(',')
        try:
            if movielensId.index(sl[1])>=0:
                print('{0},{1},{2}'.format(sl[0],sl[1],sl[2]),file=scannedRatings)
                foundMovies.append(sl[1])
        except ValueError:
            b=1    
    counter=counter+1
    
scannedRatings.close()
mvRat.close()
mapfile.close()

print(len(set(foundMovies)))
