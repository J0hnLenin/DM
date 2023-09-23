"""
4.	Напишите программу, осуществляющую переход от представления графа с помощью матрицы смежностей к представлению графа с помощью матрицы достижимости.
"""

import numpy as np
from graph_algorithms import *
from Graph import Graph
INPUT_FILE = "input.txt"

def main():
    
    try:
        adjacency_matrix = np.loadtxt(f"Input/{INPUT_FILE}", "int")
    except:
        print("File reading error.")
        return 1
  
    G = Graph(adjacency_matrix)

    print(create_accessibility_matrix(G))
         
    return 0

if __name__ == "__main__":
    main()