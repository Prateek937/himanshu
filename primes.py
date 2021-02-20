from math_ops.basic_ops import add 
from math_ops.adv_ops import multiply, divide

def isprime(a):
    if a > 1:
        for i in range(2,add(divide(a,2)[0],1)):
            q1 = divide(a,i)
            if q1[1] == 0:
                return False
        else:
            return True
    else:
        return False
    
def all_primes(a):
    ls = []
    for x in range(add(a,1)):
        if isprime(x):
            ls.append(x)
    if len(ls) > 0:
        return ls
    else:
        return "Empty list"

def prime_factors(a):
    ls = []
    for x in range(2, add(divide(a,2)[0],1)):
        if isprime(x) and divide(a,x)[1] == 0:
            ls.append(x)
    if len(ls) > 0:
        return ls
    else:
        return "Empty list"

