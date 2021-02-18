import collections
mapfile= open("mappedID.txt",'r')
movielensId=[]
for line in mapfile:
    line=line.strip()
    splitLine= line.split(',')
    intid= int(splitLine[1].strip())
    movielensId.append(intid)
mapfile.close()
'''
k=movielensId.index("7149")
print(k)
'''
movies=[]
mratings= open("movieLensRatings.txt",'r')
for line in mratings:
    line=line.strip()
    sl=line.split(',')
    intid=int(sl[1].strip())
    movies.append(intid)

'''
ctr= collections.Counter(movielensId)
k=ctr.most_common(20)
print(k)
'''
#print(len(set(movielensId)))

print(len(set(movielensId)))
print(len(set(movies)))
a=set(movielensId)
b=set(movies)
c=a-b
print(c)




    
    

