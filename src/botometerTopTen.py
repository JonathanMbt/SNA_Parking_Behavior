import matplotlib.pyplot as plt
import botometer
from commands import *
from functions import *
import statistics as st

rapidapi_key = "38940d0f3fmsh988bf0ed564bfb9p11f319jsn5db669988640"
twitter_app_auth = {
    'consumer_key': 'J2vBhcxzmgI3AkyMVBW14cG4K',
    'consumer_secret': 'CGFZU0VKDUwaUJRydcty95TcU0qShyxEkQ7M9JlyI3oOekdxJi',
    'access_token': '1386020054605647872-O42MGwS0hABOFPLhRkuW9uKpktUrBW',
    'access_token_secret': 'hnkmdunQy1NKfmR0Pb6RyEGZxazoXWmXBKaYVAVC0PNSj',
}

bom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)
users_botScore = {}
hashtags = ["#parking", "#parkinglot"]

for hashtag in hashtags:
    print("*** Please wait ! API QUERY could be a bit long. ***")
    users_id = list(getTopTen(hashtag, 10, data_filename).keys())
    users_botScore[hashtag] = {}

    query_answer = bom.check_accounts_in(users_id)
    for screen_name, result in query_answer:
        tmp = round(st.mean((result["raw_scores"]['english']['overall'], result["raw_scores"]['universal']['overall'])), 2)
        users_botScore[hashtag][str(screen_name)]= "Bot" if tmp >= 0.5 else "Human" 
    nbr_bot = list(users_botScore[hashtag].values()).count("Bot")
    labels = ["Bot", "Human"]
    values = [nbr_bot/10, (10-nbr_bot)/10]
    
    fig, ax = plt.subplots(1, 2, figsize=(12,8))
    fig.suptitle("Proportion of bots in the top 10 users for " + hashtag)
    ax[0].hist(list(users_botScore[hashtag].values()))
    ax[1].pie(values, explode=[0.1, 0], labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax[1].axis('equal')
    plt.show()

