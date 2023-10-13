"""
2.	Написать программу, реализующую алгоритм нахождения максимального потока методом Форда-Фалкерсона. 
На экран выводятся все пути от источника к стоку вместе с их величинами, найденные по ходу работы алгоритма. 
А также сама величина максимального потока.
"""

from graph_algorithms import *  

def main():

    N = random.randint(4, 6)

    G = generate_Graph(N, weight=True, orented=True)
    adj_matrix = nx.adjacency_matrix(G).todense()
    ans, way_matrix = ford(G)

    # вывод:
    print("Матрица смежности:")
    print_matrix(adj_matrix, 3, N)

    print("Путевая матрица:")
    print_matrix(way_matrix, 12, N)

    print("Наибольный поток:")
    print(ans)

    print_weight_graph(G)
    return 0

if __name__ == "__main__":
    main()