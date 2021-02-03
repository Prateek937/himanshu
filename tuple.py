def overlapping(A, B):
    start1 = A[0]
    start2 = B[0]
    end1 = A[1]
    end2 = B[1]
    if start1 < start2 and start2 < end1:
        return True


def sorting(new):
    lst = len(new)  
    for i in range(0, lst):  
          
        for j in range(0, lst-i-1):  
            if (new[j][0] > new[j + 1][0]):  
                temp = new[j]  
                new[j]= new[j + 1]  
                new[j + 1]= temp  
    return new

def redundant(A, B):
    start1 = A[0]
    start2 = B[0]
    end1 = A[1]
    end2 = B[1]
    if (start1 == start2) and (end1 == end2):
        return 1  
    elif (start1 == start2) and (end2 < end1):
        return 1  
    elif (end1 == end2) and (start1 < start2):
        return 1  
    elif (start1 < start2) and (end1 > end2):
        return 1
    else:
        return 0
    

inp_T=input().split('__')
new=[]
for i in inp_T:
  k=i.split(',')
  for j in range(len(k)):
    k[j]=int(k[j])
  new.append(tuple(k))

"""
red = []
for i in range(len(new) - 1):
    r = redundant(new[i], new[i+1])
    if r == 1:
        red.append(new[i+1])

R = []
for x in new:
    if x not in red:
        R.append(x)
res = [] 
[res.append(x) for x in R if x not in res] 

print(res)

R_Sorted = sorting(res)
print(R_Sorted)
"""

new_t = new[:]

#redundancy
for i in range(len(new)):
  for j in range(i+1, len(new)):
   if(new[i][0] <= new[j][0] and new[i][1] >= new[j][1] ):
     if(new[j] in new_t):
       new_t.remove(new[j])
new_t.sort()
print(new_t)

for i in range(len(new_t) - 1):
    if overlapping(new_t[i], new_t[i+1]):
        newl = list(new_t[i])
        newl[1] = new_t[i+1][0]
        newt = tuple(newl)
        new_t[i] = newt
print(new_t)