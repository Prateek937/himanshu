
def B(b):
    return int(str(b), 2)    


def alternating(key):
    if (len(key) < 8) or (len(key) > 16):
        return 0

    freqs = []
    for i in key:
        if key.count(i) >= 2:
            res = [j for j in range(len(key)) if key.startswith(i, j)]
            for ind in range(len(res) - 1):
                if res[ind+1] - res[ind] == 2:
                    freqs.append(i)
    final = []
    [final.append(x) for x in freqs if x not in final]
    
    if len(final) > 1:
        return 0
    elif len(final) == 0:
        return 1
    else:
        for i in final:
            if key.count(i) > 2:
                return 0
            else:
                return 1     
            


keys = list(input().split("_"))
binary = []
for i in keys:
    binary.append(alternating(i))
print(B((int("".join(map(str, binary))))))