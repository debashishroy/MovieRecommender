#id,vc,lc,dc,fc,cc format for YouTubeTrailerData.txt
def normalizeData(listToNorm):
    divider= max(listToNorm)
    if divider>0:
        for i in range(0, len(listToNorm)):
            listToNorm[i]=listToNorm[i]/divider
    return listToNorm
ts=open('TwitterSentimentScore.txt','r')
ytdata=open('YouTubeTrailerData.txt','r')
ytTs=open('YTCommentSentimentForEachMovie.txt','r')
profileFile=open('movieProfile4features.txt','w')
twitterSentiment=[]
youTubeSentiment=[]
for line in ts:
    line= line.strip()
    lineSp = line.split(',')
    sentiment= float(lineSp[1])
    twitterSentiment.append(sentiment)
    
for line in ytTs:
    line= line.strip()
    lineSp = line.split(',')
    sentiment= float(lineSp[1])
    youTubeSentiment.append(sentiment)
#print(len(twitterSentiment),len(youTubeSentiment))
vc=[]
lc=[]
dc=[]
fc=[]
cc=[]
for line in ytdata:
    line=line.strip()
    lineSp = line.split(',')
    vc.append(float(lineSp[1]))
    lc.append(float(lineSp[2]))
    dc.append(float(lineSp[3]))
    fc.append(float(lineSp[4]))
    cc.append(float(lineSp[5]))
ts.close()
ytdata.close()
ytTs.close()

vc= normalizeData(vc)
lc=normalizeData(lc)
dc=normalizeData(dc)
cc=normalizeData(cc)

for i in range(0,1000):
    print(f'{vc[i]:.5f},{lc[i]:.5f},{cc[i]:.5f},{youTubeSentiment[i]}',file=profileFile)
    

profileFile.close()






    


    
