import sys

if sys.argv[0] == "graph.py":
    # init parameters default values
    node_number = 7
    label_hashtag = False
    filename = "output_graph.png"
    graph_image = False
    not_displayed = False


    for arg in sys.argv[1:]:
        if "-" in arg:
            if arg == "--help":
                print(''' 
    -n (int) : define the number of nodes to display. 
        Default : 7 \n
    -l : Display graph with hashtag name as labels. 
        Default : False \n
    -i (filename) : Export graph as a png file (! VERY SLOW FOR LARGE GRAPH !) 
        Default filename : output_graph.png \n
    -nd : Graph is not displayed. 
        Default : False
                ''')
                exit()
            if arg == "-n": 
                node_number = int(sys.argv[sys.argv.index(arg)+1])
            elif arg == "-l":
                label_hashtag = True
            elif arg == "-i":
                filename = str(sys.argv[sys.argv.index(arg)+1])
                graph_image = True
            elif arg == "-nd":
                not_displayed = True