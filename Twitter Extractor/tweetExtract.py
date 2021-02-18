import tweepy
from tweepy import OAuthHandler
import time
import re
from time import sleep
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
'''
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
#api.update_status("Tweeting from Python application")
'''
fMovieTitles= open("movieTitlesHash.txt","r",encoding="utf8")

fileContent=fMovieTitles.readlines()
for title in fileContent:
    try:
        
        title=title.strip()
        splitTitle= title.split('::')
        movieHashTag=splitTitle[1]
        fileNameNoSymbol=re.sub(r'[^\w]','',movieHashTag)
        fileName= fileNameNoSymbol + ".txt"
        MovieTweetPath = "MovieTweets\\" + fileName
        fMovieTweets=open(MovieTweetPath,"w")
        print(fileNameNoSymbol,file=fMovieTweets)
        print(movieHashTag)
        search_words= movieHashTag+ " -filter:retweets"
        date_since ="1995-01-01"
    
        tweets= tweepy.Cursor(api.search,
                          q=search_words,
                          lang="en",
                          since= date_since).items(150)
        for tweet in tweets:
            u=tweet.text
            u=u.encode('unicode-escape').decode('utf-8')
            print(u,file=fMovieTweets)
    
        fMovieTweets.close()
    
        time.sleep(15)
    except Exception as e:
        print(str(e))
        fMovieTweets.close()
        time.sleep(60)
        pass

fMovieTitles.close()
