import numpy as np

def dijkrsta(graph, start: int = 0):
    matrix = graph.adjacency_matrix
    length = graph.length

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
    matrix = graph.adjacency_matrix
    length = graph.length

    queue = [(start, 0)]
    is_visited = [False]*length
    distance_list = [np.inf]*length 

    while queue:
        vertex, distance = queue.pop(0)
        is_visited[vertex] = True
        distance_list[vertex] = distance

        for i in range(length):
            if (not is_visited[i]) and (matrix[vertex][i]):
                queue.append((i, distance + 1))
    
    return distance_list

def create_incidence_matrix(graph) -> None:
    incidence_matrix = []
    length = graph.length

    for i in range(length):
        
        line = [False]*length
        distance_list = bfs(graph, i)

        for j in range(length):
            line[j] = (distance_list[j] != np.inf)

        incidence_matrix.append(line)

    return np.matrix(incidence_matrix)
        
