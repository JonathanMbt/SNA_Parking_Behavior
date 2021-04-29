#Parking Behaviour Analysis Project

# Python Script to construct the graph where a node represents a # 
# and an edge exists between 2 nodes, if the 2 # are in the same tweet at list once.


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from commands import *

all_hashtags = []

#reading the csv file containing all the tweets containing the #parking, #parkinglot, ...
tweets = pd.read_csv("../resources/20K_parking_data.csv")


for tweet in tweets.iloc:
    # if the tweet have hashtags
    if(type(tweet['tweet_hashtags']) == str):
        #list all Hashtags/nodes
        hashtag_of_tweet = tweet['tweet_hashtags'].split(" ")
        all_hashtags.append(hashtag_of_tweet)

# flatten array i.e. [ [a, e, b], [c, d, e]] --> [a, e, b, c, d, e]
all_hashtags = [hashtag for list_hashtag in all_hashtags for hashtag in list_hashtag]
# eliminate the duplicates in the list 
all_hashtags = list(dict.fromkeys(all_hashtags))

G = nx.Graph()
G.add_nodes_from(all_hashtags[:node_number])

# sum of consecutive number : 1+2+3+4+...+n --> n(n+1)/2
# if 3 nodes [A, B, C], we have the following edges [(A, B), (A, C), (B, C)]
# 2 (A can make 2 unique edges) + 1 (B can make 1 unique edge) + 0 (C can make 0 unique edge) = 3
# so we can easily see that the number of edge follow the following rule : nbr_node-1 + nbr_node-2 + ... + 1 + 0 = nbr_edge
# which is a sum of consecutive number so we have finally (nbr_node-1 * nbr_node)/2
edge_number = int((node_number*(node_number-1))/2)
hashtag_edges = [(i, j) for i in all_hashtags[:node_number] for j in all_hashtags[:node_number][all_hashtags[:node_number].index(i):] if (i != j) ]
G.add_edges_from(hashtag_edges)

if not label_hashtag:
    G = nx.convert_node_labels_to_integers(G,first_label=1)
    G = nx.relabel_nodes(G, lambda x: str(x))

#indicator for example
#print(nx.degree_centrality(G))

plt.plot()
nx.draw(G, with_labels=True)
plt.show()

