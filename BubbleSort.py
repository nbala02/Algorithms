def bubbleSort(values):
  for i in range(len(values)-1):
    for j in range (0, len(values)-1):
      if values[j] > values[j+1]:
        temp = values[j]
        values[j] = values[j+1]
        values[j+1] = temp
  print(values)

values = [8,3,5,2,4,9,7,0]
bubbleSort(values)
