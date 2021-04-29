#Parking Behaviour Analysis Project

# Python Script to construct the graph where a node represents a # 
# and an edge exists between 2 nodes, if the 2 # are in the same tweet at list once.


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


all_hashtags = []

#reading the csv file containing all the tweets containing the #parking, #parkinglot, ...
tweets = pd.read_csv("../resources/20K_parking_data.csv")


for tweet in tweets.iloc:
    # if the tweet have hashtags
    if(type(tweet['tweet_hashtags']) == str):
        all_hashtags.append(tweet['tweet_hashtags'].split(" "))

# flatten the array i.e. [ [a, e, b], [c, d, e]] --> [a, e, b, c, d, e]
all_hashtags = [hashtag for list_hashtag in all_hashtags for hashtag in list_hashtag]
# eliminate the duplicates in the list 
all_hashtags = list(dict.fromkeys(all_hashtags))

G = nx.Graph()
G.add_nodes_from(all_hashtags[:100])
# turn node label to integers
#G = nx.convert_node_labels_to_integers(G,first_label=1)
#G = nx.relabel_nodes(G, lambda x: str(x))

plt.plot()
nx.draw(G, with_labels=True)
plt.show()

