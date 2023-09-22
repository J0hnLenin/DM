import numpy as np
from ...graph_algorithms import *
IMPUT_FILE = "imput.txt"

def main():
    try:
        adjacency_matrix = np.loadtxt(f"Tasks/Lab_02/{IMPUT_FILE}", "int")
    except:
        print("Input error.")
        return 1
    print(adjacency_matrix)
    length = len(adjacency_matrix)
    print(dijkrsta(adjacency_matrix, length, 0))

    return 0

if __name__ == "__main__":
    main()