import pandas as pd
from openpyxl import load_workbook

path = './20K_Parking_data.csv'

df=pd.read_csv(path)
index = df.index

#This gives hastagColumn as a big list of strings, where each *string item* is in a form of list of hashtags. 
hashtagColumn = df['tweet_hashtags'].tolist()
timeColumn = df['time'].tolist()

tag = input("Enter only hashtag the data must have (with # symbol): ")

#Need to get tags with only interested hashtag
def getOnlyTag(tag):
	removeTags = []
	
	for i in range(len(hashtagColumn)):
		try:
			if ((tag.lower() + " ") not in hashtagColumn[i].lower()) and (tag.lower() != hashtagColumn[i].lower()) and (tag.lower() != hashtagColumn[i][len(hashtagColumn[i])-len(tag):].lower()):
				tweetIndex = (index[df['time'] == timeColumn[i]]).tolist()
				#For tweets made at the same time
				for j in range(len(tweetIndex)): 
					removeTags.append(tweetIndex[j])
		#This means there are tweets with no hashtags
		except AttributeError:
			#Do the same thing
			tweetIndex = (index[df['time'] == timeColumn[i]]).tolist()
			#For tweets made at the same time
			for j in range(len(tweetIndex)): 
				removeTags.append(tweetIndex[j])

	df.drop(removeTags, axis =0, inplace = True)
	return df

print('The hashtag data is being exported... Please wait...')
#Get the df
getOnlyTag(tag)
#Export df to csv file
df.to_csv(tag[1:] + '-DataSet.csv', header=True)