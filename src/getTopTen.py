import pandas as pd
import csv

df=pd.read_csv('./Parking_Data.csv')

allHashtags = df['tweet_hashtags'].tolist()
allUserId = df['user_id'].tolist()
allDateTime = df['time'].tolist()

def getTopTen(hashtag, top):
	allInfluencers = {}

	topTenInfluencers = []

	for i in range(int(len(allHashtags))):

		try:
			if hashtag+" " in allHashtags[i].lower():
				if allUserId[i] in allInfluencers:
					allInfluencers[allUserId[i]] += 1
				else:
					allInfluencers[allUserId[i]] = 1
		#This happens when there is no hashtags
		except AttributeError:
			continue

	for i in range(0, top):
		currentTop = max(allInfluencers, key=allInfluencers.get)
		topTenInfluencers.append(str(i+1)+ '. ' + str(currentTop) + ' - ' + str(allInfluencers[currentTop]) + '\n')
		allInfluencers.pop(currentTop)

	print(topTenInfluencers)

	#Create the file for top ten influencers
	topTenFile = open(hashtag[1:] +'TopTen.txt' , 'w')
	topTenFile.write("Top ten : User ID - Total number of tweets for that hashtag\n\n")
	topTenFile.writelines(topTenInfluencers)
	topTenFile.close()

top = 10
searchItem = input("Enter hastag with # you want to search: ")
getTopTen(searchItem, top)