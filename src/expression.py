from commands import *
from functions import *
import math

def supportExpression(hashtags):
    retweetCoeff = 0
    favoriteCoeff = 0
    hashtagSupport = {}

    for hashtag in hashtags:
        totalRetweets = 0
        totalFavorites = 0

        print(" \n *** " + hashtag + " *** \n")
        tweets, total = getTweet(hashtag, data_filename)

        retweetCoeff = round(1 - (total["retweets"]/(total["retweets"]+total["favorites"])), 2)
        favoriteCoeff = round(1 - (total["favorites"]/(total["retweets"]+total["favorites"])), 2)

        for tweet in tweets.values(): # tweet = {"favorites":0, "retweet": 2}
            totalRetweets += tweet["retweets"]
            totalFavorites += tweet["favorites"]
        
        print("totalFavorites", totalFavorites)
        print("totalRetweets", totalRetweets)
        support = retweetCoeff * totalRetweets + favoriteCoeff * totalFavorites
        hashtagSupport[hashtag] = support
        print("Support", support)
    
    #datasetSupport = pd.DataFrame(hashtagSupport, index=[0])
    #datasetSupport.to_csv("datasetSupport_2.csv")

    hs = hashtagSupport.copy()
    # Normalize (francesco function)
    totalSupport = sum(list(hashtagSupport.values()))
    for sup in list(hashtagSupport.keys()):
        hashtagSupport[sup] /= totalSupport 
    print("Normalization Francesco", hashtagSupport)

    # Normalize (Jonathan function)
    for sup in list(hs.keys()):
        hs[sup] = math.atan((1/100)*hs[sup]**(1/2))/(math.pi/2)
    print("Normalization Jonathan", hs)
    

def mergeDataset():
    parkingDataset = pd.read_csv("datasetSupport_1.csv")
    parkingKeys = list(parkingDataset.columns)[1:]
    parkingValues = parkingDataset.iloc[0]

    parkinglotDataset = pd.read_csv("datasetSupport_2.csv")
    parkinglotKeys = list(parkinglotDataset.columns)[1:]
    parkinglotValues = parkinglotDataset.iloc[0]

    finalDataset = {}
    for i in parkingKeys:
        if i in parkinglotKeys:
            finalDataset[i] = parkingValues[i] + parkinglotValues[i]
        else:
            finalDataset[i] = parkingValues[i]

    for i in parkinglotKeys:
        if i not in parkingKeys:
            finalDataset[i] = parkinglotValues[i]

    hs = finalDataset.copy()
    # Normalize (francesco function)
    totalSupport = sum(list(finalDataset.values()))
    for sup in list(finalDataset.keys()):
        finalDataset[sup] /= totalSupport 
    print("Normalization Francesco", finalDataset)

    # Normalize (Jonathan function)
    for sup in list(hs.keys()):
        hs[sup] = math.atan((1/100)*hs[sup]**(1/2))/(math.pi/2)
    print("Normalization Jonathan", hs)