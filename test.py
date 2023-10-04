import numpy as np
from graph_algorithms import *
import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy as sy
INPUT_FILE = "input.txt"

def main(n = 0):

    n = n + (n == 0) * random.randint(3, 7)
    nodes = [i for i in range(n)]
    edges = []
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    for i in range(n):
        for j in range(i + 1, n):
            if random.getrandbits(1):
                edges.append((i, j))
                matrix[i][j] = 1
                matrix[j][i] = 1

    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(nodes)

    M = nx.adjacency_matrix(G)
    print(M.todense())
    

    nx.draw(G)
    plt.show()


    return 0

if __name__ == "__main__":
    main()