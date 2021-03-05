def partition(values, low, high):
  pivot = values[high]
  smallestVal = low-1

  for i in range(low, high):
    if values[i] <= pivot:
      smallestVal += 1

      temp = values[smallestVal]
      values[smallestVal] = values[i]
      values[i] = temp

  temp2 = values[smallestVal+1]
  values[smallestVal+1] = values[high]
  values[high] = temp2
  return smallestVal + 1

def quickSort(values, low, high):
  if low < high:
    partitionValues = partition(values, low, high)
    quickSort(values, low, partitionValues - 1)
    quickSort(values, partitionValues + 1, high)
  
values = [10, 7, 8, 9, 5, 3, 2, 4]
print(values)
quickSort(values, 0, len(values)-1)
print(values)
