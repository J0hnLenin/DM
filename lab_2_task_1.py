"""
1.	Напишите программу, которая для неориентированного графа, заданного матрицей смежности, вычисляет его диаметр и радиус.
"""

import numpy as np
from graph_algorithms import *

def main():
    
    G = generate_Graph(n=0)
    n = len(G.nodes)
    eccentricity = []
    for i in range(n):
        distance_list = bfs(G, i)
        ecc = list(filter(lambda x:x!=np.inf, distance_list))
        eccentricity.append(max(ecc))

    print(f"Radius:   {min(eccentricity)}")
    print(f"Diameter: {max(eccentricity)}")        

    print_graph(G)
    return 0

if __name__ == "__main__":
    main()