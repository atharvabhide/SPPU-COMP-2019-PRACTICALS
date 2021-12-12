# assignment 4
def selection_sort(percentage):
    print("Original array is ", percentage)
    for i in range(len(percentage)-1):
        minimum = i
        for j in range(i+1, len(percentage), 1):
            if (percentage[j] < percentage[minimum]):
                minimum = j
        percentage[i],percentage[minimum] = percentage[minimum],percentage[i]
        print("Pass " + str(i+1) + ":" , percentage)
    return percentage

def bubble_sort(percentage):
    print("Original array is ", percentage)
    for i in range(len(percentage)-1):
        for j in range(len(percentage)-i-1):
            if percentage[j] > percentage[j+1]:
                percentage[j],percentage[j+1] = percentage[j+1],percentage[j]
        print("Pass " + str(i+1) + ":", percentage)
    return percentage

n = int(input("Enter the number of students here-\n"))
percentage = []
for i in range(n):
    element = float(input("Enter the percentage of the student-\n"))
    if element > 0:
        percentage.append(element)
choice = int(input("Enter 0 if you want to use selection sort and enter 1 if you want to use bubble sort-\n"))
if choice == 0:
    selection_sort(percentage)
else:
    bubble_sort(percentage)
print("The percentages of the students after sorting are-", percentage)
print("The percentages of top 5 students are-", percentage[-1:-6:-1])
