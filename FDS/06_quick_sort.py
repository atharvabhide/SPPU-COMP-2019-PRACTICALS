import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from shared.sorting_utils import get_student_percentages, display_top_students, partition

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

percentage = get_student_percentages()
quickSort(percentage,0,len(percentage)-1)
print("The sorted array is", percentage)
display_top_students(percentage)
