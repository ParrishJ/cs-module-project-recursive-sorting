# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    first = 0
    last = int(len(arr) - 1)
    middle_index = (first + last) // 2
    left = arr[:middle_index + 1]
    right = arr[middle_index + 1:]

    #if first <= last:
    if not arr:
        return -1
    if target == arr[middle_index]:
        return middle_index

    if target < arr[middle_index]:
        return binary_search(left, target, 0, len(left) - 1)
        
    else:
        return binary_search(right, target, 0, len(right) - 1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass


