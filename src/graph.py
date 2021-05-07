#Parking Behaviour Analysis Project

# Python Script to construct the graph where a node represents a # 
# and an edge exists between 2 nodes, if the 2 # are in the same tweet at list once.


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from commands import *
from functions import *
import statistics as st
import pygraphviz
from itertools import chain
import botometerTopTen as btt

# contains all hashtag from csv file
all_hashtags = []
all_edges = []

#reading the csv file containing all the tweets containing the #parking, #parkinglot, ...
tweets = pd.read_csv(data_filename)


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
    print("\n *** Graph exported as an image. *** \n")

# Computation Graph
if graph_properties:
    CG = nx.Graph()
    CG.add_nodes_from(hashtag_nodes)
    CG.add_edges_from(hashtag_edges)
    
    print("\n *** Global properties of Graph *** \n")
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

    graph_data['avg_shortest_path_len'] = ""
    graph_data['variance_shortest_path_len'] = ""
    for C in (CG.subgraph(c).copy() for c in components):
        tmp = nx.average_shortest_path_length(C)
        path_length = (x.values() for x in dict(nx.shortest_path_length(C)).values())
        graph_data['avg_shortest_path_len'] += str(tmp) + "/"
        path_length = list(chain.from_iterable(path_length))
        if len(path_length) > 1:
            graph_data['variance_shortest_path_len'] += str(st.variance(path_length[k] for k in path_length)) + "/"
        else:
            graph_data['variance_shortest_path_len'] += "0/"
        print("Average shortest path length: ", graph_data['avg_shortest_path_len'])
        print("Variance shortest path length: ", graph_data['variance_shortest_path_len'])
    
    graph_properties_db = pd.DataFrame(graph_data, index=[0])
    graph_properties_db.to_csv("graph_properties.csv")
    

    # 5 highest ranked nodes according to several criterias
    print("\n *** Top 5 according to different criterias *** \n")
    hgr_nodes = {}
    hgr_nodes['degree_centrality'] = maxN(degree_centrality, 5)
    print("5 highest nodes based on degree centrality: ", hgr_nodes['degree_centrality'])
    pr_centrality = nx.pagerank(CG, alpha=0.95)
    hgr_nodes['page_rank_centrality'] = maxN(pr_centrality, 5)
    print("5 highest nodes based on page rank centrality: ", hgr_nodes['page_rank_centrality'])
    closeness_centrality = nx.closeness_centrality(CG)
    hgr_nodes['closeness_centrality'] = maxN(closeness_centrality, 5)
    print("5 highest nodes based on closeness centrality: ", hgr_nodes['closeness_centrality'])
    hgr_nodes['betweenness_centrality'] = maxN(betweenness_centrality, 5)
    print("5 highest nodes based on betweenness centrality: ", hgr_nodes['betweenness_centrality'])

    # Botometer 
    hashtags_botometer = maxN(degree_centrality, 10)
    print(list(hashtags_botometer.keys()))
    print(btt.scrutinize(hashtags_botometer))
    exit()
    
    # Plot histogram of distributions 
    print("\n *** Distributions *** \n")
    fig, ax = plt.subplots(2, 2, figsize=(12,8))
    ax[0][0].hist(list(degree_centrality.values()), bins=int(node_number/2))
    ax[0][0].set_title("Distribution of the degree centrality")
    ax[0][1].hist(list(nx.clustering(CG).values()), bins=int(node_number/2))
    ax[0][1].set_title("Distribution of the local clustering coefficient")
    ax[1][0].hist(list(betweenness_centrality.values()), bins=int(node_number/2))
    ax[1][0].set_title("Distribution of the betweenness centrality")
    ax[1][1].hist(list(closeness_centrality.values()), bins=int(node_number/2))
    ax[1][1].set_title("Distribution of the closeness centrality")
    plt.show()


if not not_displayed:
    plt.figure(figsize=(12,8))
    plt.plot()
    pos = nx.drawing.nx_pydot.graphviz_layout(G, 'fdp')
    nx.draw(G, pos=pos, with_labels=True)
    plt.show()

print("\n")
