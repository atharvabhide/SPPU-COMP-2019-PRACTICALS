n = int(input("Enter the number of students-\n"))
marks = []
for i in range(n):
    element = int(input("Enter the marks-\n"))
    marks.append(element)
    
def average(marks):
    sum = 0
    len = 0
    for i in marks:
        if i != -1:
            sum += i
    for j in marks:
        if j != -1:
            len += 1
    return sum/len

def maximum(marks):
    max = -9999999
    for i in marks:
        if i == -1:
            pass
        elif i > max:
            max = i
        else:
            pass
    return max

def minimum(marks):
    min = 9999999
    for i in marks:
        if i == -1:
            pass
        elif i < min:
            min = i
        else:
            pass
    return min

def max_frequency(marks):
    distinct_elements = []
    count_of_distinct_elements = []
    for i in marks:
        if i not in distinct_elements and i!=-1:
            distinct_elements.append(i)
        else:
            pass
    for j in distinct_elements:
        count = 0
        for k in marks:
            if j == k:
                count += 1
            else:
                pass
        count_of_distinct_elements.append(count)
    max = -9999999
    for l in count_of_distinct_elements:
        max_index = 0
        if l > max or l == max:
            max = l
            max_index += 1
        else:
            pass
    return distinct_elements[max_index],max

def absent_students(marks):
    count = 0
    for i in marks:
        if i == -1:
            count += 1
        else:
            pass
    return count

print("AVERAGE OF THE CLASS IS-\n",average(marks))
print("MAXIMUM MARKS ARE-\n",maximum(marks))
print("MINIMUM MARKS ARE-\n",minimum(marks))
print("COUNT OF STUDENTS WHO ARE ABSENT IS-\n",absent_students(marks))
result = max_frequency(marks)
print("MAXIMUM OCCURING MARKS AND ITS FREQUENCY IS-\n",result[0],result[1])
