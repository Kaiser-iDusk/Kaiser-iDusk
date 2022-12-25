def co(ar, m):
	i = 0
	count = 0
	while i < m:
		if ar[i] == 1:
			count += 1
		i +=2
	return count
def ce(ar, m):
	i = 1
	count = 0
	while i < m:
		if ar[i] == 1:
			count += 1
		i +=2
	return count
for _ in range(int(input())):
	n = int(input())
	l1 = list(input())
	#print(l1)
	l = []
	for i in range(n):
		l.append(int(l1[i]))
	#print(l)
	oo = co(l, n)
	eo = ce(l, n)
	if oo >=1 and eo >= 1:
		print(1)
	else:
		print(2)
	