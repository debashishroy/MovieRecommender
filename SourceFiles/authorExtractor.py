import collections
f = open('YouTubeDataAuthor.txt','r')
#fw=open('YouTubeAuthorOnly.csv','w')
authors=[]
authid="autho:rid:::"
for line in f:
    if line.find(authid)>=0:
        authorname = line[len(authid):].strip()
        authors.append(authorname)
print(len(authors))
counter = collections.Counter(authors)
for key,value in counter.items():
    print('{0},{1}'.format(key.strip(),value))

f.close()
#fw.close()

    
