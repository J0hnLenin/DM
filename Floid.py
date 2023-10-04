"""
Для заданного графа построить матрицу кратчайших расстояний по методу Флойда-Уоршелла.
Все вычисления оформить в виде отчета. В отчете представить пошаговое решение. 
Результатом вычислений должны стать две матрицы: матрица кратчайших расстояний и путевая матрица. 
Так же представить в отчете выполненную проверку: по путевой матрице восстановить путь между двумя 
произвольными ранее несмежными вершинами. По матрице кратчайших расстояний определить кратчайшее 
расстояние для тех же самых вершин. Сверить полученные результаты с заданным графом.
"""

from graph_algorithms import *

N = 9  

def create():
    graph = nx.Graph()
    graph.add_nodes_from([i for i in range(1, N + 1)])

    graph.add_edge(1, 2, weight=22)
    graph.add_edge(1, 3, weight=13)
    graph.add_edge(1, 4, weight=12)
    graph.add_edge(2, 3, weight=14)
    graph.add_edge(2, 6, weight=16)
    graph.add_edge(3, 9, weight=13)
    graph.add_edge(4, 7, weight= 6)
    graph.add_edge(4, 9, weight= 6)
    graph.add_edge(5, 6, weight=12)
    graph.add_edge(5, 8, weight=23)
    graph.add_edge(5, 9, weight=15)
    graph.add_edge(6, 7, weight= 7)
    graph.add_edge(6, 9, weight= 8)
    graph.add_edge(7, 9, weight=13)
    graph.add_edge(8, 9, weight=19)

    return graph


def main():

    G = create() # создаём граф

    adj_matrix = nx.adjacency_matrix(G).todense()
    
    sd_matrix, way_matrix = floid(G, N)

    # проверка:
    for i in range(N):
        for j in range(N):
            summ = 0
            last = None
            for k in way_matrix[i][j]:
                if last is not None:
                    summ += adj_matrix[last - 1][k - 1]
                last = k
            if summ != sd_matrix[i][j]:
                print("Error!", summ, i, j)


    # вывод:
    print("Матрица смежности:")
    print_matrix(adj_matrix, 3)

    print("Путевая матрица:")
    print_matrix(way_matrix, 12)

    print("Матрица кратчайших расстояний:")
    print_matrix(sd_matrix, 3)

    print_weight_graph(G)
    return 0

if __name__ == "__main__":
    main()