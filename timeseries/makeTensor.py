def buildGraphFromFile(filename):
'''
This function reads in the connections from the file and generates the graph, repeats are
removed at load time.
'''

    connections = loadFile(filename)

    # build Adj list

    # format: "SourceName" : ["DestinationName", "DestinationName", ...]
    adjList = {}


    # Since the graph is undirected we have to mark the connection for the src and dest
    for transmission in connections:
        if adjList[transmission[0]]is None:
            adjList[transmission[0]] = []
        if adjList[transmission[1]]is None:
            adjList[transmission[1]] = []

        adjList[transmission[0]].append(transmission[1])
        adjList[transmission[1]].append(transmission[0])




    # build graph from list

    # return graph
