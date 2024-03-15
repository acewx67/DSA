matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(len(matrix))
print(len(matrix[0]))
col_zero_zero = matrix[0][0]
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 0:
            if col == 0:
                col_zero_zero = 0
            else:
                matrix[0][col] = 0
            matrix[row][0] = 0
# for i in (arr for arr in matrix):
#     print(i)
for i in range(len(matrix)-1,-1,-1):
    for j in range(len(matrix[0])-1,0,-1):
        if matrix[0][j] == 0 or matrix[i][0] == 0:
            matrix[i][j] = 0
if matrix[0][0] == 0:
    for i in range(len(matrix[0])-1,0,-1):
        matrix[0][i] = 0
if col_zero_zero == 0:
    for i in range(len(matrix)):
        matrix[i][0] = 0


for i in (arr for arr in matrix):
    print(i)


# find the row num and col no of 0
# guilty_rows = []
# guilty_cols = []
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         if matrix[row][col]==0:
#             guilty_rows.append(row)
#             guilty_cols.append(col)
# for row in guilty_rows:
#     for i in range(len(matrix[row])):
#         matrix[row][i] = 0
#
# for col in guilty_cols:
#     for i in range(len(matrix)):
#         matrix[i][col] = 0
# print(matrix)
