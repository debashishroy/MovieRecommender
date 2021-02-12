fMovieTitles = open ("movieTitles.txt","r")
fMovieTitlesWithHash = open ("movieTitlesHash.txt","w",encoding="utf8")
fileContent= fMovieTitles.readlines()
for title in fileContent:
    title=title.strip()
    x=title.strip()
    x=x.replace(" ","")
    x= x.replace(",","")
    x= x.replace("-","")
    x= x.replace("'","")
    x= x.replace(":","")
    x= x.replace("/","")
    x= x.replace("'\'","")
    x=x.replace("\"","")
    x=x.replace("(","")
    x=x.replace(")","")
    #x=x[:-4]
    x= '#'+ x
    print(title + "::" +x,file=fMovieTitlesWithHash)

fMovieTitles.close()
fMovieTitlesWithHash.close()
