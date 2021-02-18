import collections
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)['pos']
    return score

f = open('YouTubeTrailerComments.txt','r')
fw=open('YouTubeCommentSentimentForEachMovie.txt','w')

videoidflag="MovieID::::"
videoid=""
totScore=0.0
totLine=0
counter=0
for line in f:
    #print(line)
    if line.find(videoidflag)>=0:
        if totScore>0:
            avgScore= totScore/totLine
            print("{0},{1}".format(videoid,f'{avgScore:.2f}'),file=fw)
        counter=0
        videoid=line[len(videoidflag):].strip()
        #print(videoid)
        totScore=0.0
        totLine=0
        counter=counter+1
        continue
  
    if counter==1:
        if line.find(videoidflag)<0:
            score=sentiment_analyzer_scores(line)
            if score>0:
                totScore=totScore+score
                totLine=totLine+1


f.close()
fw.close()

'''
counter = collections.Counter(authors)
for key,value in counter.items():
    print('{0},{1}'.format(key.strip(),value))
'''




    
