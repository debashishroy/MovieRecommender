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
    developer_key="AIzaSyAEoOSkG60fa3h09UdNPV0rIcavVMHj3tQ"
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)
    for vdoId in videoIDs:
        orig_stdout = sys.stdout
        f = open('YouTubeData.txt', 'a')
        sys.stdout = f
        try:
            
            requestComment = youtube.commentThreads().list(part="snippet",
                                                maxResults=100,
                                                videoId=vdoId,
                                                textFormat="plainText")
            commentData = requestComment.execute()
            for item in commentData["items"]:
                
                comment = item["snippet"]["topLevelComment"]
                text = comment["snippet"]["textDisplay"]
                authorname=comment["snippet"]["authorDisplayName"]
                if len(text)>10:
                    print("vdo:id::: " + vdoId)
                    print("autho:rid:::" + authorname)
                    print (text)
            f.close()
        except Exception as e:
            print(str(e))
            print("------------------------------------------------------------------------------------------")
            sys.stdout = orig_stdout
            f.close()
            pass
if __name__ == "__main__":
    main()

