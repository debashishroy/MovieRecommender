import glob,os
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)['pos']
    #print("{:-<40} {}".format(sentence, str(score)))
    return score

fMovieTitles= open("movieNames.txt","r",encoding="utf8")
fileContent=fMovieTitles.readlines()
grandTotal=0
totalMovieNo=0
for movieName in fileContent:
    movieName= movieName.strip()
    movieNameWithSpace=movieName
    movieName = re.sub(r'[^\w]','',movieName)
    filePath = "Tweets\\"+ movieName + ".txt"
    counter=0
    #print(filePath)
    try:
        fTweets = open(filePath,"r",encoding="utf8")
        totScore=0
        for line in fTweets:
            score= sentiment_analyzer_scores(line)
            if score>0:
                totScore = totScore +score
                counter = counter+1
        if totScore>0:
            sentimentScore = totScore/counter
            grandTotal=grandTotal+sentimentScore
            totalMovieNo=totalMovieNo+1
            print("{0},{1}".format(totalMovieNo,f'{sentimentScore:.2f}'))
        else:
            totalMovieNo=totalMovieNo+1
            print("{0},{1}".format(totalMovieNo,0.0))
    except FileNotFoundError:
        totalMovieNo=totalMovieNo+1
        print("{0},{1}".format(totalMovieNo,0.0))
avgScore= grandTotal/totalMovieNo
print(avgScore)

