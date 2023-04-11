import numpy as np
def factor(U, j, n):
	x = U[j][j]
	if x!= 1:
		U[j] = U[j]/x
		print("Reduce: R[", j+1, "] \ ", x)
	for i in range(j+1, n):
		z = U[i][j]/U[j][j]
		U[i] -= z*U[j]
		print("Perform: R[", i+1, "] row - R[", j+1, "] row x ", z)
		print(U)
		#L[i][j] = z
	print("@U matrix: ")
	print(U)
def backfactor(U, j, n):
	for i in range(j):
		z = U[i][j] / U[j][j]
		U[i] -= z*U[j]
		print("Perform: R[", i+1, "] row - R[", j+1, "] row x ", z)
		print(U)
A = []
n = int(input("Enter the matrix size n: "))
N = int(input("Enter size of augmentation matrix: "))
for i in range(n):
	X = []
	for j in range(n+N):
		x = float(input("Enter element: "))
		X.append(x)
	A.append(X)
A = np.array(A)
print(A)
for i in range(n):
	factor(A, i, n)
for i in range(n):
	backfactor(A, n-1-i, n)
print("Final A: ")
print(A)
