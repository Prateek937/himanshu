new = [(0,10), (7,15),(8,15),(9,15),(9,27),(4,10),(2,12),(20,30), (2,12)]
new_t = new[:]

#redundancy
for i in range(len(new)):
  for j in range(i+1, len(new)):
   if(new[i][0] <= new[j][0] and new[i][1] >= new[j][1] ):
     if(new[j] in new_t):
       new_t.remove(new[j])
new_t.sort()
print(new_t)