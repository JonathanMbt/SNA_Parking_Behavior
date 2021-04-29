#Parking Behaviour Analysis Project

# Python Script to Extract tweets of a
# particular Hashtag using Tweepy and Pandas


# import modules
import pandas as pd
import tweepy


# 	#To save time: comment this out
# function to display data of each tweet
# def printtweetdata(n, ith_tweet):
# 	# print()
# 	# print(f"Tweet {n}:")
# 	# print(f"Date Created:{ith_tweet[0]}")
# 	# print(f"Username:{ith_tweet[1]}")
# 	# print(f"Description:{ith_tweet[2]}")
# 	# print(f"Location:{ith_tweet[3]}")
# 	# print(f"Following Count:{ith_tweet[4]}")
# 	# print(f"Follower Count:{ith_tweet[5]}")
# 	# print(f"Total Tweets:{ith_tweet[6]}")
# 	# print(f"Retweet Count:{ith_tweet[7]}")
# 	# print(f"Tweet Text:{ith_tweet[8]}")
# 	# print(f"Hashtags Used:{ith_tweet[9]}")
# 	# print(f"User ID:{ith_tweet[10]}")

# function to perform data extraction
def scrape(words, date_since, numtweet):
	
	# Creating DataFrame using pandas
	db = pd.DataFrame(columns=['tweetcreatedts','username', 'description', 'location', 'following',
							'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags', 'userID'])
	
	# We are using .Cursor() to search through twitter for the required tweets.
	# The number of tweets can be restricted using .items(number of tweets)
	tweets = tweepy.Cursor(api.search, q=words, lang="en",
						since=date_since, tweet_mode='extended').items(numtweet)
	
	# .Cursor() returns an iterable object. Each item in
	# the iterator has various attributes that you can access to
	# get information about each tweet
	list_tweets = [tweet for tweet in tweets]
	
	# Counter to maintain Tweet Count
	i = 1
	# To get top 10 influencers
	allInfluencers = {}
	
	# we will iterate over each tweet in the list for extracting information about each tweet
	for tweet in list_tweets:
		tweetcreatedts = tweet.created_at
		username = tweet.user.screen_name
		description = tweet.user.description
		location = tweet.user.location
		following = tweet.user.friends_count
		followers = tweet.user.followers_count
		totaltweets = tweet.user.statuses_count
		retweetcount = tweet.retweet_count
		hashtags = tweet.entities['hashtags']
		userID = tweet.user.id_str
		
		# print(hashtags)
		# Retweets can be distinguished by a retweeted_status attribute,
		# in case it is an invalid reference, except block will be executed
		try:
			text = tweet.retweeted_status.full_text
		except AttributeError:
			text = tweet.full_text
		hashtext = list()
		for j in range(0, len(hashtags)):
			hashtext.append(hashtags[j]['text'])

		#Get all influencers for a hashtag with their total number of tweets made for that hashtag
		if userID in allInfluencers:
			allInfluencers[userID] += 1
		else:
			allInfluencers[userID] = 1;

		# Here we are appending all the extracted information in the DataFrame
		ith_tweet = [tweetcreatedts, username, description, location, following,
					followers, totaltweets, retweetcount, text, hashtext, userID]
		db.loc[len(db)] = ith_tweet

		#To save time: comment this out
		# Function call to print tweet data on screen
		# printtweetdata(i, ith_tweet)
		# i = i+1

	#Get the top ten influencers from the all influencers of a hashtag
	# print(allInfluencers)
	topTenInfluencers = []
	for i in range(0, 10):
		currentTop = max(allInfluencers, key=allInfluencers.get)
		topTenInfluencers.append(("Top %s" + " : " + currentTop + " - " + str(allInfluencers[currentTop]) +"\n")%(i+1))
		#Remove from the all Influencers to get next biggest influencer 
		allInfluencers.pop(currentTop)
	print(topTenInfluencers)
	#Create the file for top ten influencers
	topTenFile = open('topTenFile.txt', 'w')
	topTenFile.write("Top : User ID - Total number of tweets for that hashtag\n\n")
	topTenFile.writelines(topTenInfluencers)
	topTenFile.close()

	filename = 'scraped_tweets.csv'
	
	# we will save our database as a CSV file.
	db.to_csv(filename)


if __name__ == '__main__':
	
	# Enter your own credentials obtained
	# from your developer account
	consumer_key = "J2vBhcxzmgI3AkyMVBW14cG4K"
	consumer_secret = "CGFZU0VKDUwaUJRydcty95TcU0qShyxEkQ7M9JlyI3oOekdxJi"
	access_key = "1386020054605647872-O42MGwS0hABOFPLhRkuW9uKpktUrBW"
	access_secret = "hnkmdunQy1NKfmR0Pb6RyEGZxazoXWmXBKaYVAVC0PNSj"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	# api = tweepy.API(auth)
	api = tweepy.API(auth, wait_on_rate_limit=True)
	
	# Enter Hashtag and initial date
	print("Enter Twitter HashTag to search for")
	words = input()
	print("Enter Date since The Tweets are required in yyyy-mm--dd")
	date_since = input()
	
	# number of tweets you want to extract in one run
	numtweet = 25000
	print("A large amount of data is being scraped, please wait few minutes...")
	scrape(words, date_since, numtweet)
	print('Scraping completed!')