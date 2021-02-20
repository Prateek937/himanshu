import math
def multiply(a,b):
    s=0
    for i in range(int(b)):
        s=s+int(a)
    return s
def divide(a,b):
	quotient=0
	remainder=0
	a=int(a)
	b=int(b)
	if a>=b:
		while a>=b:
			a=a-b
			quotient+=1
			remainder=(a)
	else:
		quotient=0
		remainder=(a)
	return (quotient,remainder)

def isdivisible(a,b):
    if divide(a,b)[1] == 0:
        return True
    else:
        return False

def factorial(a):
    return math.factorial(a)

def pow(a,b):
    return math.pow(a,b)

def reciprocal(a):
    return pow(a,-1)

def log(a):
    return math.log10(a)

