import pandas as pd
import re, csv

df=pd.read_csv('./Final - MERGEDParkingLot.csv')

#Convert from ['hashtag'] to #hashtag
#This gives hastagColumn as a big list of strings, where each *string item* is in a form of list of hashtags. 
hashtagColumn = df['hashtags'].tolist()

#Need to convert that *string item* to a list of hashtags using regular expressions in python
def conversion():
	newHashtagColumn = []
	for i in range(len(hashtagColumn)):
		# for j in range len(hashtagColumn[i])
		searchTags = hashtagColumn[i]
		regHash = re.compile(r'\w+')
		matchedHash = regHash.findall(searchTags)
		for j in range(len(matchedHash)):
			matchedHash[j] = '#' + matchedHash[j]
		newHashtagColumn.append(matchedHash)
	
	return newHashtagColumn

# print(conversion())

with open ('convertedStringTo#.csv','w',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerows(conversion())


#FINDING MAX AND MIN
p=df['retweetcount'].max()
q=df['retweetcount'].min()