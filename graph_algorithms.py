import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_Graph(n, nodes = None, edges = None, weight=False, orented=False, connected=False):

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

    if connected:
        s = random.randint(0, n - 1)
        distance = bfs(G, s)
        for i in range(n):
            if distance[i] == np.inf and not ((i, s) in edges):
                if weight:
                    G.add_edge(s, i, weight=random.randint(1, 20))
                else:
                    G.add_edge(s, i)

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

def ford(G, start, finish):
    adj_matrix = nx.adjacency_matrix(G).todense()
    N = len(adj_matrix)

    for i in range(N):
        for j in range(i + 1, N):
            if (adj_matrix[i][j] != 0):
                adj_matrix[j][i] = adj_matrix[i][j]
            else:
                adj_matrix[i][j] = adj_matrix[j][i]

    flux_matrix = np.zeros((N, N), dtype=int)
    flux_list = []
    way_list = []
    
    j = start
    while not j is None:
        k = start
        way = [(np.inf, None, start)]
        is_visited = [False]*N
        is_visited[start] = True

        while k != finish:
            j = ford_next_vertex(N, k, adj_matrix, flux_matrix, G.edges, is_visited)
            if j is None:
                if k == start:
                    break
                else:
                    k = way.pop()[2]
                    continue
        
            if (k, j) in G.edges:
                flux = adj_matrix[k][j]
            else:
                flux = flux_matrix[k][j]
            way.append((flux, j, k))
            is_visited[j] = True

            if j == finish:
                flux_list.append(min(*[x[0] for x in way]))
                ford_update_vertex(adj_matrix, flux_matrix, way, way_list, G.edges, flux_list[-1], start)
                break

            k = j
             
    return way_list, flux_list

def ford_update_vertex(adj_matrix, flux_matrix, way, way_list, edges, flux, start):
    way_list.append([])
    for step in way:
        
        if step[1] is None:
            way_list[-1].append(start)
            continue
        
        way_list[-1].append(step[1])

        if (step[2], step[1]) in edges:
            sgv = 1
        else:
            sgv = -1

        adj_matrix[step[1]][step[2]] -= flux * sgv
        flux_matrix[step[1]][step[2]] += flux * sgv

        adj_matrix[step[2]][step[1]] -= flux * sgv
        flux_matrix[step[2]][step[1]] += flux * sgv

        
        

def ford_next_vertex(N, k, adj_matrix, flux_matrix, edges, is_visited):
    maxx = 0
    next = None
    for i in range(N):
        if is_visited[i]:
            continue
        if (k, i) in edges:
            if maxx < adj_matrix[k][i]:
                maxx = adj_matrix[k][i]
                next = i
        else:
            if maxx < flux_matrix[k][i]:
                maxx = flux_matrix[k][i]
                next = i   
    return next


def find_start_and_finish(G):
    adj_matrix = nx.adjacency_matrix(G).todense()
    N = len(adj_matrix)
    start = 0
    finish = N - 1
    for j in range(N):
        is_start = True
        for i in range(N):
            if adj_matrix[i][j]:
                is_start = False
                break
        if is_start:
            start = j
            break
    
    for i in range(N):
        is_finish = True
        for j in range(N):
            if adj_matrix[i][j]:
                is_finish = False
                break
        if is_finish:
            finish = i
            break

    return start, finish

# def dfs(u, Cmin, visited = None):
#    if visited is None:
#        visited = [False]*

#    if u == t
#        return Cmin
#    visited[u] = true                  
#    for v in u.children
#        auto uv = edge(u, v)
#        if not visited[v] and uv.f < uv.c
#            int delta = dfs(v, min(Cmin, uv.c - uv.f))
#            if delta > 0
#                uv.f += delta
#                uv.backEdge.f -= delta
#                return delta
#    return 0




        
