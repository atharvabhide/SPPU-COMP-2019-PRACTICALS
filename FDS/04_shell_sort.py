import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from shared.sorting_utils import get_student_percentages, display_top_students

def shell_sort(percentage,size):
    interval = size // 2
    while interval > 0:
        for i in range(interval,size):
            temp = percentage[i]
            j = i
            while j >= interval and percentage[j - interval] > temp:
                percentage[j] = percentage[j - interval]
                j -= interval
            percentage[j] = temp
        interval = interval // 2

def insertion_sort(percentage):
    for i in range(len(percentage)):
        key = percentage[i]
        j = i - 1
        while (j >= 0 and key < percentage[j]):
            percentage[j+1] = percentage[j]
            j = j - 1
        percentage[j+1] = key

percentage = get_student_percentages()
choice = int(input("Enter 0 for shell sort and 1 for insertion sort-"))
if (choice == 0):
    shell_sort(percentage,len(percentage))
else:
    insertion_sort(percentage)
print("The sorted array is", percentage)
display_top_students(percentage)
