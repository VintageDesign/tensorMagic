import numpy as np
import time


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

start = time.time()
t = 20 # number of time slices
masterKeyIdx = 0
masterKeyList = {}
keyList = []
matrixes = []
for i in range(0, t):
    matrix, keys = buildGraphFromFile('../datasets/day2hour9/day-2_hour-9_minute-' + str(i) +'.txt')
    keyList.append(keys)
    matrixes.append(matrix)

# Create a unique list of nodes for the whole dataset
for keys in keyList:
    for key in keys:
        if masterKeyList.get(key, None) is None:
            masterKeyList[key] = masterKeyIdx
            masterKeyIdx += 1


tensor = np.zeros( (len(masterKeyList), len(masterKeyList), t), dtype=np.int8)
tIdx = 0
# Move the matrix rows and cols into the new matrix for that hour
for keys in keyList:
    for key in keys:
        oldx = keys[key]
        newx = masterKeyList[key]
        for key in keys:
            oldy = keys[key]
            if matrixes[tIdx][oldx, oldy] == 1:
                newy = masterKeyList[key]
                tensor[ newx , newy, tIdx] = matrixes[tIdx][oldx, oldy]
                tensor[ newy, newx, tIdx] = matrixes[tIdx][oldy, oldx ]

    print("Finished t = " + str(tIdx))
    tIdx += 1

print(tensor.shape)
np.savez_compressed('day_2_tensor.npz', tensor)
end = time.time()

print("Tensor saved to day_2_tensor.npz in " + str ((end - start)/60) + " minutes")
