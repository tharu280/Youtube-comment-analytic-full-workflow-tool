from dotenv import load_dotenv
import os
from googleapiclient.discovery import build


load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")
VIDEO_ID = 'bp0WaKuqSzU'
youtube = build('youtube', 'v3', developerKey=api_key)


def get_comments(video_id, max_results=100):
    comments = []
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=max_results,
        textFormat='plainText'
    ).execute()

    for item in response['items']:
        comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment_text)

    return comments


comments = get_comments(VIDEO_ID)
for idx, comment in enumerate(comments, 1):
    print(f"{idx}. {comment}")
