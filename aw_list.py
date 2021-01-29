import numpy as np

def analyse2(q, order):
	q = [int(i) for i in q]
	x = [q[i:i + order] for i in range(0, len(q), order)]
	 
	print(x)
	l1 = []
	for i in x:
		l1.append(sum(i))
	

	count_d1 = count_d2 = 0
	for i in range(order):
		count_c = c = c2 = 0
		for j in x:
			count_c += j[i]
			if x.index(j) == i:
				count_d1 += j[x.index(j)]
				count_d2 += j[order - (x.index(j)) - 1]
	
		l1.append(count_c)
	l1.append(count_d1)
	l1.append(count_d2)
	print(l1)
	counts = [l1[i:i + order] for i in range(0, len(l1), order)]
	bools = []
	for i in counts:
		if i.count(i[0]) == len(i):
			bools.append("True")
		else:
			bools.append("False")
	if bools.count("False") == 0:
		return "Truly Awesome List!"
	elif bools.index("False") == (len(bools)-1):
		return "Awesome List!"
	else:
		return "Normal List!"
		

def analyse(q, order):
	  
	arr = np.array(x)
	l1 = []
	count_d1 = count_d2 = 0
	for i in range(order):
		count_r = count_c = 0 
		count_d1 += int(arr[i][i])
		count_d2 += int(arr[i][order-i-1])
		for j in range(order):
			count_r += int(arr[i][j])
			count_c += int(arr[j][i])
		l1.append(count_r)
		l1.append(count_c)
	l1.append(count_d1)
	l1.append(count_d2)
	counts = [l1[i:i + order] for i in range(0, len(l1), order)]
	bools = []
	for i in counts:
		if i.count(i[0]) == len(i):
			bools.append("True")
		else:
			bools.append("False")
	if bools.count("False") == 0:
		return "Truly Awesome List!"
	elif bools.index("False") == (len(bools)-1):
		return "Awesome List!"
	else:
		return "Normal List!"
			
def square(q):
	m=len(q)
	if m==1:
		#it is square matrix of 1x1
		return True,1
	else:
		for i in range(1,(m+1)//2):
			if i*i==m:
				return True,i
		else:
			return False, i

q=input().split(' ')
tru,order=square(q)
if tru == True: 
	print(analyse2(q, order))
else:
	print("Invalid List!")

