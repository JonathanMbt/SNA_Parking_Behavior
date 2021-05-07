from commands import *
from functions import *

def supportExpression(hashtags):
    retweetCoeff = 0
    favoriteCoeff = 0

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

        print("Support", support)