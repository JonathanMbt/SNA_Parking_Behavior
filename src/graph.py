#Parking Behaviour Analysis Project

# Python Script to construct the graph where a node represents a # 
# and an edge exists between 2 nodes, if the 2 # are in the same tweet at list once.


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from commands import *
from functions import get_n_nodes

# contains all hashtag from csv file
all_hashtags = []


#reading the csv file containing all the tweets containing the #parking, #parkinglot, ...
tweets = pd.read_csv("../resources/20K_parking_data.csv")


for tweet in tweets.iloc:
    # if the tweet have hashtags
    if(type(tweet['tweet_hashtags']) == str):
        #list all Hashtags/nodes
        hashtag_of_tweet = tweet['tweet_hashtags'].split(" ")
        all_hashtags.append(hashtag_of_tweet)
        #if len(hashtag_of_tweet) > 1:
        #    hashtag_edges.append([(i, j) for i in hashtag_of_tweet for j in hashtag_of_tweet[hashtag_of_tweet.index(i):] if (i != j) ])

# part wich construct edges according to node_number
graph_node_edge = get_n_nodes(all_hashtags, node_number)     

# flatten array i.e. [ [a, e, b], [c, d, e]] --> [a, e, b, c, d, e]
# contains hashtag and egdes according to node_number
hashtag_nodes = [hashtag for list_hashtag in graph_node_edge[0] for hashtag in list_hashtag]
hashtag_edges = [hashtag for list_hashtag in graph_node_edge[1] for hashtag in list_hashtag]

# eliminate the duplicates in the list 
hashtag_nodes = list(dict.fromkeys(hashtag_nodes))

G = nx.Graph()
G.add_nodes_from(hashtag_nodes)
G.add_edges_from(hashtag_edges)

if not label_hashtag:
    G = nx.convert_node_labels_to_integers(G,first_label=1)
    G = nx.relabel_nodes(G, lambda x: str(x))

#indicator for example
#print(nx.degree_centrality(G))

plt.plot()
nx.draw(G, with_labels=True)
plt.show()

