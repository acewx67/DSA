matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = 0
e = len(matrix) - 1
# reverse the matrix
while s < e:
    for i in range(len(matrix[0])):
        matrix[s][i], matrix[e][i] = matrix[e][i], matrix[s][i]
    s += 1
    e -= 1
#transpose the matrix(rows turn cols or cols turn rows)
#swap the element between the rows and cols
for row in range(len(matrix)):
    for col in range(row,len(matrix)):
        t = 0
        t = matrix[row][col]
        matrix[row][col] = matrix[col][row]
        matrix[col][row] = t
print(matrix)


'''
 * clockwise rotate
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
 or
 transpose matrix and invidual row reverse
'''