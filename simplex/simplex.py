INPUT_FILE = "input.txt"
n = 3
m = 5
r = 1000
esp = 0.0000000001
def read_data():
    with open(INPUT_FILE, 'r') as f:
        
        a = [[i for i in f.readline().split()] for j in range(n)]
        
    C = a[0][0:n]
    A = [a[i][0:n] for i in range(1, n)] 
    B = [a[i][-1] for i in range(1, n)] + [0]
    
    A = [list(map(int, A[i])) for i in range(n-1)]
    B = list(map(int, B))
    C = list(map(int, C))
    
    C = [-j for j in C]

    for i in range(n):
        if (a[i][n] == 'min'):
                C = [-j for j in C]
        if (a[i][n] == '>='):
                A[i-1] = [-j for j in A[i-1]]
    
    Z = [[0]*(n-1) for i in range(n)]
    for i in range(n-1):
        Z[i][i] = 1
    
    M = [A[i] + Z[i] for i in range(n-1)]
    M.append(C + Z[n-1])
    
    return M, B

def find_ans(M, B):
    ans = [0]*m
    t = 0
    for j in range(m):
        c = 0
        for i in range(n):
            
            if (M[i][j] >= esp or M[i][j] <= -esp):
                
                c += 1
                t = M[i][j]

        if c == 1:
            ans[j] = B[j] / t 
    return ans          

        


def test(M):
    return min(M[-1]) >= 0

def smx(M, B):
    X = [0]*(n-1)
    for _ in range(r):
        if not test(M):
            X_set = set()        
            jx = M[-1].index(min(M[-1]))
            for i in range(n-1):
                X[i] = B[i] / M[i][jx]
                if X[i] > 0:
                    X_set.add(X[i])
            ix = X.index(min(X_set))
            xx = M[ix][jx]
            for i in range(n):
                if i == ix:
                    continue
                k = -1 * M[i][jx] / xx
                for j in range(m):
                    M[i][j] += k * M[ix][j]
                B[i] += k * B[ix]
        else:
            return find_ans(M, B)
    return None
    
def main():
    M, B = read_data()
    
    ans = smx(M, B)

    if ans is None:
        print("Не удалось найти оптимальное решение")
    else:

        print("Оптимальное решение:")     
        for i in range(m):
            print(f"x[{i}] = {ans[i]}")
    return



if __name__ == '__main__':
    main()