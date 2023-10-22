def binary_search(val,arr):
    arr.sort()
    low, high = 0, len(arr) - 1
    mid = (low+high) // 2

    while low <= high:
        mid = (low+high) // 2
        
        if arr[mid] == val:
            return arr[mid]
        elif arr[mid] < val:
            high = mid
        else:
            low = mid
    return None
    