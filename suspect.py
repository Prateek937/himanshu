l1 = list(input().split('###'))
percentage = list(l1[3].split(" "))
list_pair = []
for i in range(len(l1[0])):
    pair = []
    if l1[0][i] != ' ':
        pair.append(l1[0][i])
        pair.append(l1[1][i])
        list_pair.append(pair)

split_len = []
split_len.append((len(list_pair)*int(percentage[0]))//100)
if l1[2] != 'False':
    split_len.append((len(list_pair)*int(percentage[1]))//100)
    split_len.append(len(list_pair)- (split_len[0]+split_len[1]))
else:
    split_len.append(len(list_pair)- split_len[0])
index = 0
splitted = []
for length in split_len:
    temp = []
    for i in range(length):
        temp.append(list_pair[index])
        index += 1
    splitted.append(temp)

for i in splitted:
    for x, y in i:
        print(x + "" + y, end=' ')
    if splitted.index(i) != (len(splitted)-1):
        print("###", end="")
print()


