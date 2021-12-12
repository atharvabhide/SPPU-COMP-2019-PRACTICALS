# magic square
n = int(input("Enter the number of rows or columns-\n"))
l1 = []
check_row = []
check_column = []
check_diagonal_1 = []
check_diagonal_2 = []
flag = True

for i in range(n):
    l2 = []
    for j in range(n):
        element = int(input("Enter the element-\n"))
        l2.append(element)
    l1.append(l2)

for i in l1:
    row_sum = 0
    for j in i:
        row_sum += j
    check_row.append(row_sum)

for i in range(len(l1)):
    if check_row[i] != check_row[0]:
        flag = False
        break
    
for i in range(n):
    column_sum = 0
    for j in range(n):
        column_sum += l1[j][i]
    check_column.append(column_sum)

for i in range(len(l1)):
    if check_column[i] != check_column[0]:
        flag = False
        break
        
for i in range(len(l1)):
    diagonal_1_sum = 0
    for j in range(len(l1)):
        diagonal_1_sum += l1[j][j]
    check_diagonal_1.append(diagonal_1_sum)
    
if flag == True:
    for i in range(len(l1)):
        if check_diagonal_1[i] != check_diagonal_1[0]:
            flag = False
            break
        
for i in range(len(l1)):
    diagonal_2_sum = 0
    for j in range(len(l1)):
        diagonal_2_sum += l1[j][n-j-1]
    check_diagonal_2.append(diagonal_2_sum)
    
if flag == True:
    for i in range(len(l1)):
        if check_diagonal_2[i] != check_diagonal_2[0]:
            flag = False
            break

if flag == True:
    print("Yes it is a magic square")
else:
    print("No it is not a magic square")
