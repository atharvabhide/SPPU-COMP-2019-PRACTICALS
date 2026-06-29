"""Shared utilities for sorting-related practicals."""


def get_student_percentages():
    """Read student percentages from stdin, validating range [0, 100]."""
    n = int(input("Enter the number of students here-\n"))
    percentages = []
    for i in range(n):
        element = float(input("Enter the percentage of the student here-\n"))
        if 0.0 <= element <= 100.0:
            percentages.append(element)
    return percentages


def display_top_students(sorted_percentages, count=5):
    """Display the top `count` students from a sorted (ascending) list."""
    print(f"The top {count} students are-")
    for p in sorted_percentages[-1:-(count + 1):-1]:
        print(p, end=' ')
    print()


def partition(array, low, high):
    """Lomuto partition scheme using the last element as pivot.

    Returns the final index of the pivot.
    """
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1
