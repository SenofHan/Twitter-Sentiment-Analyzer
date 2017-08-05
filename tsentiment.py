import tweepy
from textblob import TextBlob

consumer_key = 'JmlR9oW0MIVv6fheadaHK3L7w'
consumer_secret = 'tCimaCXUWuIxk3CEC8oAHZntma2YdZH9VL4whNfQRF16E7QOPr'

access_token = '892580133931859968-ncDUE7hhCZW7VSysGO4PS95wgMw95jR'
access_token_secret = 'eP8dYvFU4DsXT5BfqsJ1RWZXS1oX64N0NMUhvhcgvGAi2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

target = input('What would you like to analyze?')

public_tweets = api.search(target)

f = open('results.csv', 'w') 

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0.2:
        print(tweet.text,', positive', file=f)
    elif analysis.sentiment.polarity > 0:
        print(tweet.text,', neutral', file=f)
    else:
        print(tweet.text,', negative', file=f)
f.close()
    
