import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_Graph(n, nodes = None, edges = None, weight=False, orented=False):

    if nodes is None or edges is None:
        
        nodes = [i for i in range(n)]
        edges = []
            
        for i in range(n):
            for j in range(i + 1, n):
                if random.getrandbits(1):
                    edges.append((i, j))

    if orented:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    G.add_nodes_from(nodes)
    if weight:
        for edge in edges:
            G.add_edge(edge[0], edge[1], weight=random.randint(1, 20))
    else:
        G.add_edges_from(edges)
    return G

def is_oriented(graph) -> bool:
    matrix = nx.adjacency_matrix(graph).todense()
    length = len(matrix)
    
    for i in range(length):
        for j in range(i + 1, length):
            if matrix[i][j] != matrix[j][i]:
                return True
    return False    
    
def print_graph(graph):
    nx.draw(graph, with_labels = True)
    plt.show()

def print_weight_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels = True)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

def dijkrsta(graph, start: int = 0):
    matrix = nx.adjacency_matrix(graph).todense()
    length = len(matrix)

    is_visited = [False]*length
    distance_list = [np.inf]*length 
    distance_list[start] = 0
    nearly = start 
    while nearly != -1:

        is_visited[nearly] = True

        for i in range(length):
            distance = distance_list[nearly] + (matrix[nearly][i] if matrix[nearly][i] != 0 else np.inf)
            distance_list[i] = min(distance_list[i], distance)
        
        nearly = -1
        for i in range(length):    
            if (not is_visited[i]) and ((nearly == -1) or (distance_list[i] <= distance_list[nearly])):    
                
                nearly = i
        
    return distance_list

def bfs(graph, start: int = 0):
    matrix = nx.adjacency_matrix(graph).todense()
    
    length = len(matrix)

    queue = [(start, 0)]
    is_visited = [False]*length
    distance_list = [np.inf]*length 
    
    while queue:
        vertex, distance = queue.pop(0)
        if is_visited[vertex]:
            continue
        
        is_visited[vertex] = True
        distance_list[vertex] = distance

        for i in range(length):
            if (not is_visited[i]) and (matrix[vertex][i]):
                queue.append((i, distance + 1))
    
    return distance_list

def create_accessibility_matrix(graph) -> None:
    accessibility_matrix = []
    matrix = nx.adjacency_matrix(graph).todense()
    length = len(matrix)

    for i in range(length):
        
        line = [False]*length
        distance_list = bfs(graph, i)

        for j in range(length):
            line[j] = (distance_list[j] != np.inf)

        accessibility_matrix.append(line)

    return np.matrix(accessibility_matrix)

def print_matrix(Matrix, t, N):
    print(" ", end=' ')
    for i in range(N):
        print(str(i).ljust(t), end=' ')
    print()

    for i in range(N):
        print(i, end=' ')
        for j in range(N):
            print(str(Matrix[i][j]).ljust(t), end=' ')
        print()
    print()

def floid(G):
    # Инициализируем матрицы:
    # adj_matrix - смежности
    # sd_matrix  - путевая
    # way_matrix - кратчайших расстояний

    adj_matrix = nx.adjacency_matrix(G).todense()
    N = len(adj_matrix)
    sd_matrix = []

    for i in range(N):
        sd_matrix.append([(j if j != 0 else np.inf) for j in adj_matrix[i]])
        sd_matrix[i][i] = 0

    way_matrix = [[[] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if sd_matrix[i][j] != np.inf:
                way_matrix[i][j] = [i, j]
    
    # заполняем матрицы:
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if sd_matrix[i][j] > sd_matrix[i][k] + sd_matrix[k][j]:
                    sd_matrix[i][j] = sd_matrix[i][k] + sd_matrix[k][j]
                    way_matrix[i][j] = way_matrix[i][k][:-1] + way_matrix[k][j]
    return sd_matrix, way_matrix

def ford(G):
    adj_matrix = nx.adjacency_matrix(G).todense()
    N = len(adj_matrix)

    way_matrix = [[[] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if adj_matrix[i][j] != 0 or i==j:
                way_matrix[i][j] = [i, j]

             

    return 0, way_matrix

def dfs(u, Cmin, visited = None):
   if visited is None:
       visited = [False]*

   if u == t
       return Cmin
   visited[u] = true                  
   for v in u.children
       auto uv = edge(u, v)
       if not visited[v] and uv.f < uv.c
           int delta = dfs(v, min(Cmin, uv.c - uv.f))
           if delta > 0
               uv.f += delta
               uv.backEdge.f -= delta
               return delta
   return 0


        
