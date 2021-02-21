import time
import factorial as fact

inp=int(input())
t1=time.time()
a=fact.factorial_rec(inp)
t2=time.time()
a1=time.time()
b=fact.factorial_nonrec(inp)
a2=time.time()
q=(t2-t1)*1000
w=(a2-a1)*1000
if q>w:
  print("Winner : factorial_nonrec")
else:
  print("Winner : factorial_rec")
print("factorial_rec : ",q)
print("factorial_nonrec :",w)
