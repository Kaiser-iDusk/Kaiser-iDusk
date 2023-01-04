#L-U Decomposition 	
def factor(U, L, j, n):
	x = U[j][j]
	for i in range(j+1, n):
		y = U[i][j]
		z = y/x
		for t in range(n):
			U[i][t] -= z*(U[j][t])
		L[i][j] = z
	print("U matrix: ")
	print(U)
	print("L matrix: ")
	print(L)
A = []
n = int(input("Enter the matrix size n: "))
for i in range(n):
	B = []
	for j in range(n):
		x = int(input("Enter  element: "))
		B.append(x)
	A.append(B)
L = []
for i in range(n):
	C =[]
	for j in range(n):
		if i==j:
			C.append(1)
		else:
			C.append(0)
	L.append(C)
print("L matrix @init: ")
print(L)
print("U matrix @init:")
print(A)
for i in range(n):
	factor(A, L, i, n)