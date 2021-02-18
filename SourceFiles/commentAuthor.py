import collections
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)['pos']
    #print("{:-<40} {}".format(sentence, str(score)))
    return score

f = open('YouTubeDataAuthor.txt','r')
fw=open('YouTubeAuthorSentiment.txt','w')
authors=[]
videos=[]
authid="autho:rid:::"
videoid="vdo:id::: "
videoidname=""
authorname=""
counter=0
for line in f:
    if line.find(videoid)>=0:
        counter=0
        videoidname=line[len(videoid):].strip()
        videos.append(videoidname)
        counter=counter+1

    if line.find(authid)>=0:
        authorname = line[len(authid):].strip()
        authors.append(authorname)
        counter=counter+1
        continue
      
    if counter==2:
        if line.find(videoid)<0:
            score=sentiment_analyzer_scores(line)
            if score>0:
                print("{0},{1},{2}".format(videoidname,authorname,f'{score:.2f}'),file=fw)
            #print(videoidname,authorname,line)
    

f.close()
fw.close()
print(len(authors))
print(len(videos))
'''
counter = collections.Counter(authors)
for key,value in counter.items():
    print('{0},{1}'.format(key.strip(),value))
'''


#fw.close()

    
