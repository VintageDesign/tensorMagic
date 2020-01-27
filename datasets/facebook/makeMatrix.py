import numpy as np


filename = 'facebook0'

edges = open(filename+'.txt', "r").readlines()

nodeSet = set()
for edge in edges:
    nodes = edge.split()
    nodes = (int(nodes[0]), int(nodes[1]))

    nodeSet.add(nodes[0])
    nodeSet.add(nodes[1])

nodeSet = list(nodeSet)
matrix = np.ndarray((len(nodeSet), len(nodeSet)))


for edge in edges:
    nodes = edge.split()
    start = nodeSet.index(int(nodes[0]))
    end   = nodeSet.index(int(nodes[1]))
    matrix[start, end] = 1
    matrix[end, start] = 1


np.savez_compressed(filename+'.npz', matrix)
