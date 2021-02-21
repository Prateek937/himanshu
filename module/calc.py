import basic_ops
import adv_ops
from fractions import Fraction

def validate(q):
    if q.replace(',','').isdigit() or q.replace('(','').replace(')','').replace(',','').isdigit():
        if q.replace(',','').isdigit() and q[0].isdigit() and q[-1].isdigit():
            return True, "digit"
            print('YeS without brackets')
        elif (((q.endswith(')') and q.startswith('(')) and q.count('),(')==1 and q.count(',')==3) or ((q.startswith('(') and q.endswith(')')) and q.count(',')==1)):
            if ((q.startswith('(') and q.endswith(')')) and q.count(',')==1):
                return True, "single" 
                print('with brackets valid but single')
            else:
                return True, "double"
                print('with two pairs of ccordinate')
        else:
            return False, "no"
    else:
        return False, "no"
#nothing
def ins(text):
    b, c = validate(text)
    if b and c == "double": 
        n = 2
        if text[0] == "(" and text[-1] == ")":
            groups = text.split(',')
            a, b = ','.join(groups[:n]), ','.join(groups[n:])
        try:
            a = a.replace("(","")
            a = list(a.replace(")","").split(","))
            b = b.replace("(","")
            b = list(b.replace(")","").split(","))
            l =  a+b
            return float(Fraction(int(l[0]), int(l[1]))), float(Fraction(int(l[2]), int(l[3])))
        except ValueError:
            print("Invalid input1")
            exit()
    elif b and c == "single":
        text = text.replace("(", "")
        text = list(text.replace(")", "").split(","))
        try:
            return float(Fraction(int(text[0]), int(text[1])))
        except TypeError:
            print("Invalid input")
            exit()
    elif b:
        if "," in text:
            return text.split(",")
        else:
            return text
    else:
        print("Invalid input")
        exit()

print("""
Menu:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Factorial
7. Reciprocal
8. Log
9. Quit
""")
choice = input("Enter your choice:")


if(choice=='1'):
    text  = input("Enter two numbers to perform addition:")
    a, b = ins(text)
    print(basic_ops.add(float(a),float(b))) 
elif(choice=='2'):
    text = input("Eneter two numbers to perform subtraction:")
    a, b = ins(text)
    print(basic_ops.sub(float(a),float(b)))
elif(choice=='3'):
    text = input("Enter two numbers to perform multiplication:")
    a, b = ins(text)
    print(adv_ops.multiply(float(a),float(b)))
elif(choice=='4'):
    text = input("Enter two numbers to perform division:")
    a, b = ins(text)
    print(adv_ops.divide(float(a),float(b)))
elif(choice=='5'):
    text = input("Enter two numbers to perform power:")
    a, b = ins(text)
    print(adv_ops.pow(float(a),float(b)))
elif(choice=='6'):
    text = input("Enter a numbers to perform factorial:")
    a = ins(text)
    print(adv_ops.factorial(float(a)))
elif(choice=='7'):
    text = input("Enter a numbers to perform reciprocal:")
    a = ins(text)
    print(adv_ops.reciprocal(float(a)))
elif(choice=='8'):
    text = input("Enter a numbers to perform logarithm:")
    a = ins(text)
    print(adv_ops.log(float(a)))
elif(choice=='9'):
    exit()
