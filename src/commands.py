import sys

data_filename = "../resources/20K_parking_data.csv"

if sys.argv[0] == "graph.py":
    # init parameters default values
    node_number = 7
    label_hashtag = False
    filename = "output_graph.png"
    graph_image = False
    not_displayed = False
    graph_properties = False
    botoMeter = False
    expression = False

    for arg in sys.argv[1:]:
        if "-" in arg:
            if arg == "--help":
                print(''' 
    -n (int) : define the number of nodes to display. 
        Default : 7 \n
    -l : Display graph with hashtag name as labels. 
        \n
    -i (filename) : Export graph as a png file (! VERY SLOW FOR LARGE GRAPH !) 
        Default filename : output_graph.png \n
    -nd : Graph is not displayed. 
        \n
    -p : Calculate basics graph properties 
        \n
    -f (filename) : Use data from the specified filename. Only csv files are supported. 
        Check github to get the valid csv format. \n
    -b : Scrutinize top 25 users (tell the proportion of bot and human) for each hashtag in top 10 hastags in terms of degree centrality
        \n
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
            elif arg == "-p":
                graph_properties = True
            elif arg == "-f":
                data_filename = str(sys.argv[sys.argv.index(arg)+1])
            elif arg == "-b":
                botoMeter = True
            elif arg == "-e":
                expression = True