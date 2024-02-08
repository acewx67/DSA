numRows = 5
list = []
for i in range(1, numRows + 1):
    arr = [0] * i
    list.append(arr)
for i in range(numRows):
    list[i][0] = 1
    list[i][len(list[i])-1] = 1
for i in range(numRows):
    for j in range(len(list[i])):
        if list[i][j] == 0:
            list[i][j] = list[i-1][j-1]+list[i-1][j]
for i in list:
    print(i)