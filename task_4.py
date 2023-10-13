"""
4.	Напишите программу, осуществляющую переход от представления графа с помощью матрицы смежностей к представлению графа с помощью матрицы достижимости.
"""

from graph_algorithms import *

def main():
    
    G = generate_Graph(n=0)

    print(nx.adjacency_matrix(G).todense())
    print(create_accessibility_matrix(G))
    print_graph(G)
         
    return 0

if __name__ == "__main__":
    main()