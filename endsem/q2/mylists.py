def mean_list(l , N , M):
    mean_list = []
    for i in range(N):
        mean = 0
        for j in range(M):
            mean+=l[j][i]
        mean_list.append("{:.2f}".format(mean/M))
        mean_list = [float(i) for i in mean_list]
    return mean_list

def distance(l1, l2, N):
    distance = 0
    for i in range(N):
        distance += (l1[i] - l2[i])**2

    distance = "{:.2f}".format(distance**0.5)
    return distance

def closest_farthest(main_list , key_list , M , N):
    d_max = 0
    d_min = 0
    for i in range(M):
        d1 =distance(main_list[i] , key_list , N)
        if i == 0:
            d_min , d_max ,closest,farthest = d1 , d1 , main_list[i] , main_list[i]
        else:
            if d1 > d_max :
                d_max = d1
                farthest = main_list[i]
            elif d1<d_min:
                d_min = d1
                closest = main_list[i]

    return closest , farthest

def is_in_set(l1, l2):
    if l2 in l1:
        return True
    else:
        return False

