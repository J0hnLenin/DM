"""
2.	Написать программу, реализующую алгоритм нахождения максимального потока методом Форда-Фалкерсона. 
На экран выводятся все пути от источника к стоку вместе с их величинами, найденные по ходу работы алгоритма. 
А также сама величина максимального потока.
"""

from graph_algorithms import *  

def main():

    N = 5
    G = generate_Graph(N, weight=True, orented=True, connected=True)

    # Ищем исток и сток. Если таких несколько, берём с наименьшим индексом. 
    # Если таких нет - назначаем истоком вершину 0, стоком - вершину n-1
    start, finish = find_start_and_finish(G)

    adj_matrix = nx.adjacency_matrix(G).todense()
    ways, fluxs = ford(G, start, finish)

    # вывод:
    print("Матрица смежности:")
    print_matrix(adj_matrix, 3, N)

    print(f"Исток: {start}")
    print(f"Сток: {finish}")
    print()
    print("Величины путей и пути:")
    for i in range(len(ways)):
        print(fluxs[i], ways[i])
    print()
    print("Наибольный поток:")
    print(sum(fluxs))

    print_weight_graph(G)
    return 0

if __name__ == "__main__":
    main()