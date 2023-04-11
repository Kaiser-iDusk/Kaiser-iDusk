#cofactor
def cof(j, C, S):
    for i in range(1, len(C)):
        t = 0
        s = []
        if j == len(C) - 1: 
            while(t<len(C)-1):
                s.append(C[i][t])
                t+=1
        else:
            while t < len(C): 
                if t == j:
                    t += 1
                s.append(C[i][t])
                t += 1 
        S.append(s)
#computations
def my_rec_det(n, L):
    if n == 1:
        return L[0][0]
    else:
        S = []
        sum = 0
        for j in range(n):
            cof(j, L, S)
            sum += ((-1)**j) * my_rec_det(n-1, S) * L[0][j]
            S = []
        return sum
#main
n = int(input())
A = []
for i in range(n):
    B = list(map(int, input().split()))
    A.append(B)
print("Determinant is ", my_rec_det(n, A))