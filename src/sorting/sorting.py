# TO-DO: complete the helper function below to merge 2 sorted arrays
test_arr = [1, 2, 3, 4]
test_arr_b = [5, 6]

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    

    # Your code here
    count = 0
    while arrA or arrB:
        #count = len(merged_arr) - ((len(arrA)) + (len(arrB)))
        if len(arrA) != 0 and len(arrB) == 0:
            merged_arr[count] = arrA[0]
            arrA.pop(0)
            count += 1
        elif len(arrB) != 0 and len(arrA) == 0:
            merged_arr[count] = arrB[0]
            arrB.pop(0)
            count += 1
        elif arrA[0] < arrB[0]:
            merged_arr[count] = arrA[0]
            arrA.pop(0)
            count += 1
        elif arrB[0] < arrA[0]:
            merged_arr[count] = arrB[0]
            arrB.pop(0)
            count += 1 
 
    print(merged_arr)


    return merged_arr

merge(test_arr, test_arr_b)

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    pass
    #return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
