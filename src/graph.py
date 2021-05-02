#Parking Behaviour Analysis Project

# Python Script to construct the graph where a node represents a # 
# and an edge exists between 2 nodes, if the 2 # are in the same tweet at list once.


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from commands import *
from functions import get_n_nodes
import statistics as st
import pygraphviz
import pandas as pd

# contains all hashtag from csv file
all_hashtags = []
all_edges = []

#reading the csv file containing all the tweets containing the #parking, #parkinglot, ...
tweets = pd.read_csv("../resources/20K_parking_data.csv")


for tweet in tweets.iloc:
    # if the tweet have hashtags
    if(type(tweet['tweet_hashtags']) == str):
        #list all Hashtags/nodes
        hashtag_of_tweet = tweet['tweet_hashtags'].split(" ")
        all_hashtags.append(hashtag_of_tweet)
        if len(hashtag_of_tweet) > 1:
            all_edges.append([(i, j) for n, i in enumerate(hashtag_of_tweet) for j in hashtag_of_tweet[n+1:]])

# part wich construct edges according to node_number
graph_node_edge = get_n_nodes(all_hashtags, node_number)     

# flatten array i.e. [ [a, e, b], [c, d, e]] --> [a, e, b, c, d, e]
# contains hashtag and egdes according to node_number
hashtag_nodes = [hashtag for list_hashtag in graph_node_edge[0] for hashtag in list_hashtag]
all_hashtags = [hashtag for list_hashtag in all_hashtags for hashtag in list_hashtag]
all_edges = [edge for list_edge in all_edges for edge in list_edge]
hashtag_edges = [hashtag for list_hashtag in graph_node_edge[1] for hashtag in list_hashtag]

# eliminate the duplicates in the list 
hashtag_nodes = list(dict.fromkeys(hashtag_nodes))

# Displayed Graph
G = nx.Graph()
G.add_nodes_from(hashtag_nodes)
G.add_edges_from(hashtag_edges)

if not label_hashtag:
    G = nx.convert_node_labels_to_integers(G,first_label=1)
    G = nx.relabel_nodes(G, lambda x: str(x))

if graph_image:
    graph = nx.drawing.nx_agraph.to_agraph(G)
    graph.graph_attr.update(nodesep=4)
    graph.draw(filename+".png", prog="fdp")
    print("*** Graph exported as an image. ***")

# Computation Graph
CG = nx.Graph()
CG.add_nodes_from(hashtag_nodes)
CG.add_edges_from(hashtag_edges)

print("*** Global properties of Graph ***")
graph_data = {}
graph_data['node_number'] = len(CG.nodes)
print("Number of nodes: ", graph_data['node_number'])
graph_data['edge_number'] = len(CG.edges)
print("Number of edges: ", graph_data['edge_number'])
degree_centrality = nx.degree_centrality(CG)
graph_data['avg_degree_centrality'] = st.mean(degree_centrality[k] for k in degree_centrality)
print("Average degree centrality: ", graph_data['avg_degree_centrality'])
graph_data['variance_degree_centrality'] = st.variance(degree_centrality[k] for k in degree_centrality)
print("Variance degree centrality: ", graph_data['variance_degree_centrality'])
betweenness_centrality = nx.betweenness_centrality(CG)
graph_data['avg_betweenness_centrality'] = st.mean(betweenness_centrality[k] for k in betweenness_centrality)
print("Average betweenness centrality: ", graph_data['avg_betweenness_centrality'])
graph_data['variance_betweenness_centrality'] = st.variance(betweenness_centrality[k] for k in betweenness_centrality)
print("Variance betweenness centrality: ", graph_data['variance_betweenness_centrality'])
components = [CG.subgraph(c).copy() for c in nx.connected_components(CG)]
graph_data['diameter'] = max([nx.diameter(x) for x in components])
print("Diameter: ", graph_data['diameter'])
graph_data['clustering_coefficient'] = nx.average_clustering(CG)
print("Clustering Coefficient:", graph_data['clustering_coefficient'])
graph_data['size_lg_component'] = len(max(components, key=len))
print("Size of largest component: ", graph_data['size_lg_component'])

graph_properties_db = pd.DataFrame(graph_data, index=[0])
graph_properties_db.to_csv("graph_properties.csv")

""" from itertools import chain
for C in (CG.subgraph(c).copy() for c in nx.connected_components(CG)):
    path_lengths = (x.values() for x in dict(nx.shortest_path_length(C)).values())
    print(path_lengths)
    tmp = sum(chain.from_iterable(path_lengths))
    tmp /= graph_data['node_number']*(graph_data['node_number']-1)
    #print(nx.average_shortest_path_length(C))
    print("average_shortest_path_length: ", tmp) """

if not not_displayed:
    plt.plot()
    pos = nx.drawing.nx_pydot.graphviz_layout(G, 'fdp')
    nx.draw(G, pos=pos, with_labels=True)
    plt.show()