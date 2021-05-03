import operator
import pandas as pd

def get_n_nodes(arr, n):
    """
        Return n nodes and all the corresponding edges.
    """
    hashtag_nodes = []
    hashtag_edges = []
    nbr_nodes = 0

    for hashtags in arr:
        if (nbr_nodes + len(hashtags)) <= n:
            hashtag_nodes.append(hashtags)
            hashtag_edges.append([(i, j) for n,i in enumerate(hashtags) for j in hashtags[n+1:]])
            nbr_nodes += len(hashtags)
        else:
            diff = nbr_nodes + len(hashtags) - n
            hashtag_nodes.append(hashtags[:-diff])
            hashtag_edges.append([(i, j) for n, i in enumerate(hashtags[:-diff]) for j in hashtags[:-diff][n+1:]])
            tmp_hashtag_nodes = [hashtag for list_hashtag in hashtag_nodes for hashtag in list_hashtag]
            nbr_nodes += len(hashtags[:-diff])
            real_nodes = len(list(dict.fromkeys(tmp_hashtag_nodes)))
            if real_nodes >= n:
                break
            else:
                nbr_nodes = real_nodes
                diff = nbr_nodes - (len(hashtags) - diff) + len(hashtags) - n
                hashtag_nodes[len(hashtag_nodes)-1] = hashtags[:-diff]
                hashtag_edges[len(hashtag_nodes)-1] = [(i, j) for n, i in enumerate(hashtags[:-diff]) for j in hashtags[:-diff][n+1:]]
                nbr_nodes += len(hashtags[:-diff])
    return [hashtag_nodes, hashtag_edges]

def maxN(arr, n):
    """
        Return the top-n element in a list/dict
    """
    if type(arr) == list:
        return sorted(arr, reverse=True)[:n]
    else:
        return dict(sorted(arr.items(), key=operator.itemgetter(1), reverse=True)[:n])

def getTopTen(hashtag, top, csv_file, file_output = False):

    df=pd.read_csv(csv_file)

    allHashtags = df['tweet_hashtags'].tolist()
    allUserId = df['user_id'].tolist()
    allDateTime = df['time'].tolist()
    allInfluencers = {}

    topTenInfluencers = []

    for i in range(int(len(allHashtags))):  
    	try:
    		if hashtag+" " in allHashtags[i].lower():
    			if allUserId[i] in allInfluencers:
    				allInfluencers[allUserId[i]] += 1
    			else:
    				allInfluencers[allUserId[i]] = 1
    	#This happens when there is no hashtags
    	except AttributeError:
    		continue
    if file_output:      
        for i in range(0, top):
            currentTop = max(allInfluencers, key=allInfluencers.get)
            topTenInfluencers.append(str(i+1)+ '. ' + str(currentTop) + ' - ' + str(allInfluencers[currentTop]) + '\n')
            allInfluencers.pop(currentTop)  
        return topTenInfluencers
    else:
        return maxN(allInfluencers, top)  
