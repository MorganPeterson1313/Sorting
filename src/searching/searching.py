# STRETCH: implement Linear Search				
def linear_search(arr, target):
  n = len(arr)
  for i in range(0, n):
    if( arr[i] == target):
      return i
  
  # TO-DO: add missing code

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
  
  low = 0
  high = len(arr)-1
  #mid =(low+high)//2

  while low <= high:
    mid = low + (high-1)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1



  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty

  if arr[middle]== target:
    return middle

  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle + 1 )
  else:
    return -1
  # TO-DO: add missing if/else statements, recursive calls
