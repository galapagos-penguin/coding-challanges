def find_smallest_int(arr):
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
    return smallest
