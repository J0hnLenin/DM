import networkx as nx
import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self, matrix = None, n = 0):
        if matrix is None:
            
            n = n + (n == 0) * random.randint(3, 7)
            self.nodes = [i for i in range(n)]
            self.edges = []
            matrix = []
            for i in range(n):
                matrix.append([0]*n)
            for i in range(n):
                for j in range(i + 1, n):
                    if random.getrandbits(1):
                        self.edges.append((i, j))
                        matrix[i][j] = 1
                        matrix[j][i] = 1

        else:
            self.length = len(matrix)
            self.adjacency_matrix = matrix
            self.nodes = []
            self.edges = []

    
    def is_oriented(self) -> bool:
        for i in range(self.length):
            for j in range(i + 1, self.length):
                if self.adjacency_matrix[i][j] != self.adjacency_matrix[j][i]:
                    return True
        return False    
    
    def print_graph(self):

        G = nx.Graph()
        G.add_nodes_from(self.nodes)
        G.add_edges_from(self.edges)
        nx.draw(G)
        plt.show()