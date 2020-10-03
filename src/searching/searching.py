# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    """ first = 0
    last = int(len(arr) - 1)  """
    middle_index = (start + end) // 2
    """ left = arr[:middle_index + 1]
    right = arr[middle_index + 1:] """

    

    #if first <= last:
    if end >= 1:

        if target == arr[middle_index]:
            return middle_index

        elif target > arr[middle_index]:
            return binary_search(arr, target, middle_index + 1, end)

        else:
            return binary_search(arr, target, start, middle_index - 1)
            
        
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    first = 0
    last = int(len(arr) - 1)
    middle_index = (first + last) // 2
    left = arr[:middle_index + 1]
    right = arr[middle_index + 1:]

    #if first <= last:
    if not arr:
        return -1

    if arr[0] < arr[-1]:
        if target == arr[middle_index]:
            return middle_index

        if target < arr[middle_index]:
            return agnostic_binary_search(left, target)
            
        else:
            return agnostic_binary_search(right, target)
    if arr[0] > arr[-1]:
        if target == arr[middle_index]:
            return middle_index

        if target < arr[middle_index]:
            return agnostic_binary_search(right, target)
            
        else:
            return agnostic_binary_search(left, target) 



