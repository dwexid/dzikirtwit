import json
import pandas as pd
import matplotlib.pyplot as plt
import re


def main():


	#Reading Tweets
	print('Reading Tweets\n')
	tweets_data_path = 'dzikirtwit.txt'
	#tweets_data = json.load(open(tweets_data_path, 'r'))

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        result = re.sub(r"http\S+", "", tweet['text'])
	        tweet['text'] = result
	        tweets_data.append(tweet)
	    except:
	        continue

	#with open('dzikirtwit.json', 'w') as outfile:
	#	outfile.write(json.dumps(tweets_data, indent=4, sort_keys=True))

	#Structuring Tweets
	print('Structuring Tweets\n')
	tweets = pd.DataFrame.from_dict(tweets_data, orient='columns')
	pd2 = tweets.groupby('lan').count().sort_values('text', ascending=False).reset_index()
	print(pd2)

if __name__=='__main__':
	main()
