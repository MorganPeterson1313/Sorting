# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i=0
    j=0
    k=0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1

        else:
            merged_arr[k] = arraB[j]
            k= k+1
            j= j+1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k = k+1
        i = i+1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k =k+1
        j =j+1
    return merged_arr
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr)> 1:
        mid = len(arr)//2 # finding the middle of the Array
        L = arr[:mid] # dividing the array elements
        R = arr[mid:] # into two halves

        merge_sort(L)
        merge_sort(R) 

        #copyingto temp arrays L[] and R[]
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
        else:
            arr[k] = R[j]
            j+=1
            k+=1

        #checking to see if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
