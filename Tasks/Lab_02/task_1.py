import numpy as np

IMPUT_FILE = "imput.txt"

def rad_dim(matrix, length):

    r = np.inf
    d = -1

    is_visited = [False]*length
    queue = [0]
    while queue:
        i = queue.pop(0)
        is_visited[i] = True
        
        for j in range(length):
            if is_visited[j] or not matrix[i][j]:
                continue
            queue.append(j)
            
        


    return 0

def main():
    try:
        adjacency_matrix = np.loadtxt(IMPUT_FILE)
    except:
        print("Input error.")
        return 1
    length = len(adjacency_matrix)
    radius, diameter = rad_dim(adjacency_matrix, length)
    return 0

if __name__ == "__main__":
    main()