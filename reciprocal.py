def no_input(string):
    if string == "":
        raise IOError("No input was given!")
    

string = input()
try:
    no_input(string)
except IOError as err:
    print(err)
    print("Execution completed!")
    exit()
    
l1 = list(string.split(" "))
for i in l1:
    try:
        j = float(i)
        print("1/{}".format(i))
    except ValueError:
        print("Coud not convet into int or float: ", i)
        
print("Execution completed!")
