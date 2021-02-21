# write code for factorial.py here
def factorial_rec(a):
  if a==0:return 1
  else:
    return a * factorial_rec(a-1)

def factorial_nonrec(a):
  s=1
  for i in range(1,a+1):
    s=s*i
    a-=1
  return s


# write code for main.py here
