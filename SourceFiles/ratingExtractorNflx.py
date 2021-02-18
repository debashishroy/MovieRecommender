f = open('combined_data_1.txt',"r")
fmapid= open('mappedID.txt','r')
mapids= fmapid.readlines()
fmapid.close()

i=0
found=0
movieID=""
for r in f:
    fnetFlix=open('netflixRating.txt',"a")
    r=r.strip()
    colon=":"
    if colon in r:
        movieID= r[:-1]
        print(movieID)
        i=i+1
        found=0
        for ids in mapids:
            splitids=ids.split(",")
            if movieID == splitids[0]:
                found=1
                print("Match found for", movieID)
                break
    else:    
        if found==1:
            splitR= r.split(",")
            print('{},{},{}'.format(movieID, splitR[0],splitR[1]),file=fnetFlix)
            
    
    if(i==2127):
        break

f.close()
fnetFlix.close()

