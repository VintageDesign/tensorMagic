import numpy as np


def loadFile(filename):
    lines = []
    f = open(filename, 'r')
    rawLines = f.readlines()
    f.close()

    for line in rawLines:
        temp = line.split(",")
        temp = (temp[0], temp[1][:-2])
        lines.append(temp)

    return set(lines)

def buildGraphFromFile(filename):
    '''
    This function reads in the connections from the file and generates the graph, repeats are
    removed at load time.
    '''

    connections = loadFile(filename)

    # build Adj list

    # format: "SourceName" : ["DestinationName", "DestinationName", ...]
    adjList = {}
    keys = {}
    currentKeyIdx = 0


    for transmission in connections:
        if adjList.get(transmission[0], None) is None:
            adjList[transmission[0]] = []
            keys[transmission[0]] = currentKeyIdx
            currentKeyIdx += 1
        if adjList.get(transmission[1], None) is None:
            adjList[transmission[1]] = []
            keys[transmission[1]] = currentKeyIdx
            currentKeyIdx += 1

        adjList[transmission[0]].append(transmission[1])

    # build graph from list
    n = len(adjList)
    adjMatrix = np.zeros((n,n))

    for row, values in adjList.items():
        src = keys[row]
        for col in values:
            dest = keys[col]
            # Since the graph is undirected we have to mark the connection for the src and dest
            adjMatrix[src, dest] = 1
            adjMatrix[dest, src] = 1





    # return graph
    return adjMatrix, keys



matrix, keys = buildGraphFromFile('../datasets/day2/day-2_hour-11.txt')

print(matrix.shape)
