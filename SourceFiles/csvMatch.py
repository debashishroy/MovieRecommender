mlFile= open("movies.csv","r",encoding = "ISO-8859-1")
nfFile=open("Netflix_movie_titles.csv","r",encoding = "ISO-8859-1")
mlFileContent= mlFile.readlines()
nfFileContent=nfFile.readlines()
mlFile.close()
nfFile.close()
i=0
count=0
for nfrow in nfFileContent:
    splitNFrow= nfrow.split(",")
    nfMovieTitle = splitNFrow[2].strip()
    nfMovieID= splitNFrow[0].strip()
    #print(nfMovieTitle)
    
    for mlrow in mlFileContent:
        splittedRow = mlrow.split(",")
        mlMovieTitle=splittedRow[1].strip()
        mlMovieID=splittedRow[0].strip()
        if nfMovieTitle in mlMovieTitle:
            print(nfMovieTitle)
            #print(nfMovieID,",",mlMovieID)
            count=count+1
            break
    
    if(count==1000):
        break
    
print("done")
        
    
