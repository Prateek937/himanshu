class FormulaError(Exception): 
  pass

def inp(element):
    test1=element.split()
    if len(test1)>3 or len(test1)<3:
      raise FormulaError("Input has less or more than three elements")
    element1,sign,element2=test1
    try:
      element1=float(element1)
      element2=float(element2)
    except ValueError:
      raise FormulaError("First and Third element must be an integer or float value.")
    except TypeError:
      raise FormulaError("Check out the types of the elements.")
    try:
        if sign not in ["+","-","*","/"]:
            raise FormulaError("Invalid operator.")
        return print(calculator(element1,sign,element2))
    except FormulaError as err:
        print(err)

def calculator(e1,sign,e2):
  if sign=='+':
    return e1+e2
  elif sign=="-":
    return e1-e2
  elif sign=="*":
    return e1*e2
  elif sign=="/":
    if e2==float(0):
      raise FormulaError("Cannot divide by zero")
    else:
      return e1/e2

while True:
  enter_values=input()
  if enter_values=='quit':
    break
  inp(enter_values)