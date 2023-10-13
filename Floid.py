"""
1.	Написать программу, реализующую алгоритм Флойда-Уоршелла для нахождения матрицы кратчайших расстояний 
(результаты – матрица длин кратчайших путей и матрица самих кратчайших путей, а также восстановление кратчайшего пути, 
соединяющего две заданные пользователем вершины).
"""

from graph_algorithms import *  

def main():

    N = random.randint(4, 6)

    G = generate_Graph(N, weight=True)
    adj_matrix = nx.adjacency_matrix(G).todense()
    sd_matrix, way_matrix = floid(G)

    # проверка:
    for i in range(N):
        for j in range(N):
            summ = 0
            last = None
            for k in way_matrix[i][j]:
                if last is not None:
                    summ += adj_matrix[last][k]
                last = k
            if summ != sd_matrix[i][j] and summ != 0:
                print("Error!", summ, i, j)


    # вывод:
    print("Матрица смежности:")
    print_matrix(adj_matrix, 3, N)

    print("Путевая матрица:")
    print_matrix(way_matrix, 12, N)

    print("Матрица кратчайших расстояний:")
    print_matrix(sd_matrix, 3, N)

    print_weight_graph(G)
    return 0

if __name__ == "__main__":
    main()