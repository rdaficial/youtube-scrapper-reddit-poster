import requests
import praw

CLIENT_ID = ''
CLIENT_SECRET = ''
REDDIT_PASSWORD = ''
REDDIT_USERNAME = ''

GOOGLE_API_KEY = ''

channel_id = ''
subreddit = ''

def post_to_reddit(title, url):
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         password=REDDIT_PASSWORD,
                         user_agent='test script',
                         username='')

    print(reddit.user.me())

    title = title
    url = url
    sr = subreddit
    reddit.subreddit(sr).submit(title, url=url)


def get_video_details():

    r = requests.get(
        'https://www.googleapis.com/youtube/v3/search?key=' + GOOGLE_API_KEY + '&channelId=' + channel_id + '&part=snippet,id&order=date&maxResults=20').json()
    title = r['items'][0]['snippet']['title']
    video_id = r['items'][0]['id']['videoId']
    url = 'https://www.youtube.com/watch?v=' + video_id

    print(title)
    print(video_id)
    print(url)

    return title,url

if __name__ == "__main__":

    title,url = get_video_details()

	#value = ""
    #if value in title:
    #    print("match")
	
	post_to_reddit(title, url)

    #else:
    #    print("no match")
