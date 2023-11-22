lista = [1,4,7,2,3,23,42,0,95,124,983,23]

def bubble_sort(arr):
  n = len(arr)
  
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        
  return arr
print(bubble_sort(lista))      