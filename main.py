import json, urllib, time, tweepy
from secrets import twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret, youtube_api_key

def search_new_video():
    # twitter/tweepy connection
    twitter_auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    twitter_auth.set_access_token(twitter_access_token, twitter_access_token_secret)
    twitter_api = tweepy.API(twitter_auth)

    # youtube connection & formatting links
    youtube_channel_id = 'YouTube Channel ID'

    youtube_base_video_url = 'https://www.youtube.com/watch?v='
    youtube_api_url = 'https://www.googleapis.com/youtube/v3/search?'

    youtube_url = youtube_api_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(youtube_api_key, youtube_channel_id)
    youtube_input = urllib.request.urlopen(youtube_url)
    youtube_response = json.load(youtube_input)

    video_id = youtube_response['items'][0]['id']['videoId']

    # check if a new video has been uploaded
    video_exists = False
    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != video_id:
            link = youtube_base_video_url + video_id
            tweet = 'Message: ' + link
            twitter_api.update_status(status=tweet)
            print('Tweeted')
            video_exists = True
    
    if video_exists:
        with open('videoid.json', 'w') as json_file:
            data = {'videoId' : video_id}
            json.dump(data, json_file)

try:
    while True:
        search_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('Stopping script')
