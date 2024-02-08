matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(len(matrix))
print(len(matrix[0]))
# find the row num and col no of 0
guilty_rows = []
guilty_cols = []
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col]==0:
            guilty_rows.append(row)
            guilty_cols.append(col)
for row in guilty_rows:
    for i in range(len(matrix[row])):
        matrix[row][i] = 0

for col in guilty_cols:
    for i in range(len(matrix)):
        matrix[i][col] = 0
print(matrix)