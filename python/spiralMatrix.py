matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
t,b,l,r = 0,len(matrix)-1,0,len(matrix[0])-1
list = []
while t <= b:
    i = l
    while(i <= r and t <=b and l<=r):
        list.append(matrix[t][i])
        i += 1
    t += 1
    i = t
    while(i <= b and t <=b and l<=r):
        list.append(matrix[i][r])
        i += 1
    r -= 1
    i = r
    while(i >= l and t <=b and l<=r):
        list.append(matrix[b][i])
        i -= 1
    b -= 1
    i = b
    while i >= t and t <=b and l<=r:
        list.append(matrix[i][l])
        i -= 1
    l += 1
print(list)