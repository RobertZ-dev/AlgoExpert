def binarySearch(array, target):
    # Write your code here.
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == array[middle]:
            return middle
        elif target > array[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


# array = [8, 5, 2, 9, 5, 6, 3]
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
print(binarySearch(array, 33))
