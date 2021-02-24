try:
    import mylists

    def readtxt(filename):
        file1 = open(filename, 'r')
        lines = file1.readlines()
        lines_list = []
        for x in lines:
            x = x.replace("\n", "")
            lines_list.append(list(x.split(",")))
                 
        if len(lines_list) == 0:
            print("Empty file")
            exit()
        initial_length = len(lines_list)
        count = 0
        flag = 0
        for x in lines_list:
            if len(x) != 5:
                flag = 1
                count += 1
                lines_list.pop(lines_list.index(x))
            elif len(x) == 5:
                for p in x:
                    try:
                        p = float(p)
                    except:
                        flag = 1
                        lines_list.pop(lines_list.index(x))

        final_length = len(lines_list)
        if initial_length - final_length == initial_length:
            print("Invalid Content")
            exit()  
        if flag == 1:
            print("Some rows are skipped")
        file1.close()
        lines_list1 = []
        for x in lines_list:
            lines_list1.append([float(i) for i in x])
        
        return lines_list1, len(lines_list[0]), len(lines_list)

    def key_validate(key_list, N):
        if len(key_list) != N:
            print("Invalid key")
            exit()
        else:
            for x in key_list:
                if type(x) == float:
                    pass
                else:
                    print("Invalid key")
                    exit()

    key_list = input("key_list:")
    try:
        key_list = list(map(float, key_list.replace("[", "").replace("]", "").split(',')))
    except:
        print("Invalid key")
        exit()
    key_validate(key_list, 5)
    lines, N, M = readtxt("lists.txt")
    meanL = mylists.mean_list(lines, N, M)
    print("Mean list:", meanL)
    print("Distance mean_list-key_list:", mylists.distance(meanL, key_list, N))
    closest, farthest = mylists.closest_farthest(lines, key_list, M, N)
    print("closest_list:", closest)
    print("distance of closest-key_list:", mylists.distance(closest, key_list, N))
    print("farthest_list:", farthest)
    print("distance of farthest-key_list:", mylists.distance(farthest, key_list, N))
    print("distance closest-farthest:", mylists.distance(closest, farthest, N))
except IOError:
    print("IOError : Input output error raised!")
except ValueError as err:
    print(err)
    print("ValueError : Value error check formats!")
except ZeroDivisionError:
    print("ZeroDivisionError : cannot divide by zero !")
except ImportError:
    print("ImportError Exception : unable to locate the module !")
except EOFError:
    print("EOFError : File ended but still program is reading!")
except KeyboardInterrupt:
    print("KeyboardInterrrupt : program encountered a halt by user!")
except TypeError:
    print("TypeError : check out format of data")
except NameError:
    print("NameError : Name not defined  or variable used before assignment")