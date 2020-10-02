# TO-DO: complete the helper function below to merge 2 sorted arrays
test_arr = [1, 5, 3, 2]
#test_arr_b = [5, 6]

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    count = 0

    while arrA or arrB:
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
 
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
   
    #base case
    if len(arr) <= 1:
        return arr 
    #if len(arr) > 1:
    first = 0
    last = int(len(arr) - 1)
    middle_index = (first + last) // 2
    left = arr[:middle_index + 1]
    right = arr[middle_index + 1:]       
        
    #sorted_arr = merge(left, right)
    
    return merge(merge_sort(left), merge_sort(right))

merge_sort(test_arr)

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
