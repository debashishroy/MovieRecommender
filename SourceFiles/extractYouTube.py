import os
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import sys
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    
    csv_file ="vdoLinks.csv"
    inc=0
    df = pd.read_csv(csv_file)
    videoIDs = df['youtubeId']
    
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    developer_key=""
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)
    for vdoId in videoIDs:
        orig_stdout = sys.stdout
        f = open('YouTubeData.txt', 'a')
        sys.stdout = f
        try:
            print(vdoId)
            requestComment = youtube.commentThreads().list(part="snippet",
                                                maxResults=100,
                                                videoId=vdoId,
                                                textFormat="plainText")
            commentData = requestComment.execute()
            for item in commentData["items"]:
                comment = item["snippet"]["topLevelComment"]
                text = comment["snippet"]["textDisplay"]
                if len(text)>10:
                    print (text)
        
            requestStats = youtube.videos().list(part="snippet,contentDetails,statistics",id=vdoId)
            statisticsData=requestStats.execute()
            description=""
            viewCount=""
            likeCount=""
            dislikeCount=""
            favoriteCount=""
            commentCount=""
            duration=""
            definition=""
            description=statisticsData['items'][0]['snippet']['description']
            viewCount=statisticsData['items'][0]['statistics']['viewCount']
            likeCount=statisticsData['items'][0]['statistics']['likeCount']
            dislikeCount=statisticsData['items'][0]['statistics']['dislikeCount']
            favoriteCount=statisticsData['items'][0]['statistics']['favoriteCount']
            commentCount=statisticsData['items'][0]['statistics']['commentCount']
            duration=statisticsData['items'][0]['contentDetails']['duration']
            definition=statisticsData['items'][0]['contentDetails']['definition']
            print(viewCount,likeCount,dislikeCount,favoriteCount,commentCount)
            print(description)
            print(duration)
            print(definition)
            
            print("------------------------------------------------------------------------------------------")
            sys.stdout = orig_stdout
            f.close()
        except Exception as e:
            print(str(e))
            print("------------------------------------------------------------------------------------------")
            sys.stdout = orig_stdout
            f.close()
            '''
            print(viewCount,likeCount,dislikeCount,favoriteCount,commentCount)
            print(description)
            print(duration)
            print(definition)
            '''
            pass
        if inc==20:
            break
        else:
            inc =inc+1

if __name__ == "__main__":
    main()

