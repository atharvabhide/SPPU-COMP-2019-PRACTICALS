def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

n = int(input("Enter the number of students here-\n"))
percentage = []
for i in range(n):
    element = float(input("Enter the percentage of the student here-\n"))
    if (0.0 <= element <= 100.0):
        percentage.append(element)
quickSort(percentage,0,len(percentage)-1)
print("The sorted array is", percentage)
print("The top 5 students are-")
for i in percentage[-1:-6:-1]:
    print(i, end=' ')
