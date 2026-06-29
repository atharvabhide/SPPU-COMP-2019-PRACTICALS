# assignment 4
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from shared.sorting_utils import get_student_percentages, display_top_students

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

percentage = get_student_percentages()
choice = int(input("Enter 0 if you want to use selection sort and enter 1 if you want to use bubble sort-\n"))
if choice == 0:
    selection_sort(percentage)
else:
    bubble_sort(percentage)
print("The percentages of the students after sorting are-", percentage)
display_top_students(percentage)
