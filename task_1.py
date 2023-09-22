import numpy as np
from graph_algorithms import *
from Graph import Graph
IMPUT_FILE = "input.txt"

def main():
    
    try:
        adjacency_matrix = np.loadtxt(f"Input/{IMPUT_FILE}", "int")
    except:
        print("File reading error.")
        return 1
    G = Graph(adjacency_matrix)
    if not G.is_oriented():
        print("Graph is not oriented")
        return 1
    
    distance_list = bfs(G)
    eccentricity = list(filter(lambda x:x!=0, distance_list))
    print(f"Radius:   {min(eccentricity)}")
    print(f"Diameter: {max(eccentricity)}")        

    return 0

if __name__ == "__main__":
    main()