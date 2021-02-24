try:
    import mylists

    def readtxt(filename):
        file1 = open(filename, 'r')
        lines = file1.readlines()
        lines_list = []
        for x in lines:
            x = x.replace("\n", "")
            temp = list(x.split(","))
            lines_list.append([float(i) for i in temp]) 
        if len(lines_list) == 0:
            print("Empty file")
            exit()
        intial_length = len(lines_list)
        count = 0
        for x in lines_list:
            if len(x) != 5:
                flag = 1
                count += 1
                lines_list.pop(lines_list.index(x))
        
        final_length = len(lines_list)
        if intial_length == final_length and flag == 1:
            print("Invalid Content")
            exit()  
        elif flag == 1:
            print("Some rows are skipped")
        return lines_list, len(lines_list[0]), len(lines_list)

    def key_validate(key_list, N):
        print("1")
        print(len(key_list))
        if len(key_list) != N:
            print("Invalid key")
            exit()
        else:
            for x in key_list:
                print("2")
                if type(x) == int:
                    pass

    key_list = input()
    try:
        key_list = list(map(float , key_list.replace("[", "").replace("]", "").split(',')))
        key_validate(key_list, 5)
    except:
        print("Invalid key1")
        exit()
    lines, N, M = readtxt("lists.txt")
    print(type(lines))
    meanL = mean_list(lines, N, M)
    print("Mean list: ", meanL)
    print("Distance mean_list-key_list", distance(meanL, key_list, N))
    closest, farthest = closest_farthest(lines, key_list, M, N)
    print(lines, meanL)
    print("closest_list: ", closest, end=",")
    print("distance of closest-key_list", distance(closest, key_list, N), end="")
    print("farthest_list: ", farthest, end=",")
    print("distance of farthest-key_list", distance(closest, key_list, N))
    print("distance closest-farthest", distance(closest, farthest, N))



except IOError as i:
  print(i)
except ValueError as m:
  print(m)
except ZeroDivisionError as t:
  print(t)
except ImportError as Ie:
  print(Ie)
except EOFError as eof:
  print(eof)
except KeyboardInterrupt:
  print("KeyboardInterrrupt : program encountered a halt by user")
