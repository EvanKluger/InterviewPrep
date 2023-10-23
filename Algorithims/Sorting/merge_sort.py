def merge_sort(arr):
    n = len(arr)
    n_split = n // 2
    
    if n <= 1:
        return arr
    
    arr1 = arr[:n_split]
    arr2 = arr[n_split:]

    sorted_arr1 = merge_sort(arr1)
    sorted_arr2 = merge_sort(arr2)

    return merge(sorted_arr1, sorted_arr2)



def merge(arr1, arr2):
    merged = []
    left_idx, right_idx = 0, 0

    n1 = len(arr1)
    n2 = len(arr2)

    while left_idx < n1 and right_idx < n2:
        if arr1[left_idx] < arr2[right_idx]:
            merged.append(arr1[left_idx])
            left_idx += 1
        else:
            merged.append(arr2[right_idx])
            right_idx += 1
        
    while left_idx < n1:
        merged.append(arr1[left_idx])
        left_idx += 1
    
    while right_idx < n2:
        merged.append(arr2[right_idx])
        right_idx += 1
    
    return merged

    


    

    
    
    