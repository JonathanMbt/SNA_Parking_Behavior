from collections import Counter

def get_n_nodes(arr, n):
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
