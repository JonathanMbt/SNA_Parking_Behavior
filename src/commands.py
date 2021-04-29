import sys

if sys.argv[0] == "graph.py":
    # init parameters default values
    node_number = 7
    label_hashtag = False


    for arg in sys.argv[1:]:
        if "-" in arg:
            if arg == "--help":
                print(''' 
    -n (int) : define the number of nodes to display. Default : 7 \n
    -l : Display graph with hashtag name as labels. Default : False
                ''')
                exit()
            if arg == "-n": 
                node_number = int(sys.argv[sys.argv.index(arg)+1])
            elif arg == "-l":
                label_hashtag = True