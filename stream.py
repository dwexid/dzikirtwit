import tweepy
import json

access_token = "1076751755793227776-IHV38OMEk9kErghw7aWaMjwmDk6k5Y"
access_token_secret = "pqDnp2srC21g7bhbrZjCY5PkX5KjBuPG9t1pDTflmkr1g"
consumer_key = "2YMbnv7OD1NBz6as08NY7L1FD"
consumer_secret = "Cb4DTFNdWpW0yDBAZx7N97fRnWY1LgMSPtXMolYzOpz7ubvBwE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#keywords = ['HR.%20Bukhori OR HR%20Aisyah OR HR.%20Muslim OR HR.%20Tirmidzi OR %23Hadits']
keywords = ['allahuakbar OR alhamdulillah OR subhanallah OR astagfirullah OR allah']
for tweet in tweepy.Cursor(api.search,q=keywords, since="2018-12-1").items():
	if (not tweet.retweeted) and ('RT @' not in tweet.text):
		data = {}
		data['text'] = tweet.text
		data['lan'] = tweet.lang
		data = json.dumps(data)
		print(data)