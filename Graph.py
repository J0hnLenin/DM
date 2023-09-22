class Graph:
    def __init__(self, matrix):
        self.length = len(matrix)
        self.adjacency_matrix = matrix
        self.incidence_matrix = None
    
    def is_oriented(self) -> bool:
        for i in range(self.length):
            for j in range(i + 1, self.length):
                if self.adjacency_matrix[i][j] != self.adjacency_matrix[j][i]:
                    return False
        return True
    
    