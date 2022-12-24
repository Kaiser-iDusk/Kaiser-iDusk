import sys
sys.setrecursionlimit(10**6)
def sqrt(x, a, count, j):
	t = (x+(a/x))/2
	
	if j!= count:
			j+=1
			sqrt(t, a, count, j)
	elif j == count:
		print(t)

print("Enter the value : \n")
y = int(input())
print("Precision: \n")
z = int(input())
sqrt(1, y, z, 1)
	