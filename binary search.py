import sys
import time
sys.setrecursionlimit(1000000)
def bin_search(query, hi, lo, array):
	middle = (hi+lo)//2
	if array[middle] == query:
		print("element at ",middle, " is the query ")
	elif array[middle] > query:
		lo = middle +1
		bin_search(query, hi, lo, array)
	else:
		hi = middle -1 
		bin_search(query, hi, lo, array)

give = list(map(int, input().split()))
query = int(input())
start = time.time()
bin_search(query, 0, len(give)-1, give)
stop = time.time()
print("Programme  executed in ", (stop - start)*10**3, "ms.")