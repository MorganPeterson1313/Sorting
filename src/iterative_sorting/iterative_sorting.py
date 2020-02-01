# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
    for j in range(cur_index, len(arr)):
        if arr[smallest_index] >arr[j]:
            smallest_index = j



        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    smallest_index = 0
    cur_index = smallest_index + smallest_index[1]
    swap_flag = False
    while swap_flag == True:
        swap_flag == False
    for j in range( cur_index, len(arr[smallest_index] + 1)):
        if j > arr[smallest_index]:
            arr[smallest_index] = arr[cur_index]
            swap_flag == True




    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr