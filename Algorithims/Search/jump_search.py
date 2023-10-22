def jump_search(val, arr):
    arr.sort()
    n_arr = len(arr)
    step = int(n_arr**.5)
    curr_step = step
        
    prev = 0
    while arr[min(curr_step, n_arr)-1] < val:
        prev = curr_step
        curr_step += step
        if prev >= n_arr:
            return None
        
    for i in range(prev,min(curr_step,n_arr)):
        if arr[i] == val:
            return arr[i]
    return None



