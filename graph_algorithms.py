import numpy as np

def dijkrsta(matrix: list, length: int, start: int):
    
    is_visited = [False]*length
    distance_list = [np.inf]*length 
    distance_list[start] = 0
    nearly = start

    while nearly != -1:

        is_visited[nearly] = True
        distance_list[nearly]
        for i in range(length):
            distance = distance_list[nearly] + (matrix[nearly][i] if matrix[nearly][i] != 0 else np.inf)
            distance_list[i] = min(distance_list[i], distance)
        
        nearly = -1
        for i in range(length):    
            if (not is_visited[i]) and ((nearly == -1) or (distance_list[i] <= distance_list[nearly])):    
                nearly = i
        
    return distance_list