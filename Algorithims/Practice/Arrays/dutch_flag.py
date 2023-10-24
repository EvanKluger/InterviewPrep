#dutch flag problem
#arr has RED,WHITE,BLUE


def dutch_flag_prob(arr):
    RED, WHITE, BLUE = range(3)
    n = len(arr)
    red_idx = 0
    white_idx = 0
    blue_idx = n-1

    while white_idx <= blue_idx:
        if arr[white_idx] == WHITE:
            white_idx += 1

        elif arr[white_idx] == BLUE:
            arr[white_idx], arr[blue_idx] = arr[blue_idx], arr[white_idx] 
            blue_idx -= 1
        
        elif arr[white_idx] == RED:
            arr[white_idx], arr[red_idx] = arr[red_idx], arr[white_idx] 
            red_idx += 1 
            white_idx += 1
    return arr

print(dutch_flag_prob([0, 0, 0, 0]))  # [0, 0, 0, 0]
print(dutch_flag_prob([1, 1, 1, 1]))  # [1, 1, 1, 1]
print(dutch_flag_prob([2, 2, 2, 2]))  # [2, 2, 2, 2]
print(dutch_flag_prob([1, 2, 0, 1, 2, 0]))  # [0, 0, 1, 1, 2, 2]
print(dutch_flag_prob([0, 0, 1, 1, 2, 2]))
print(dutch_flag_prob([2, 2, 1, 1, 0, 0]))
print(dutch_flag_prob([1, 0, 2, 1, 2, 0, 1, 0, 2]))  # [0, 0, 0, 1, 1, 1, 2, 2, 2]
print(dutch_flag_prob([0, 0, 0, 1, 1, 1]))  # [0, 0, 0, 1, 1, 1]
print(dutch_flag_prob([1, 1, 1, 2, 2, 2]))  # [1, 1, 1, 2, 2, 2]
print(dutch_flag_prob([0, 0, 0, 2, 2, 2]))  # [0, 0, 0, 2, 2, 2]
print(dutch_flag_prob([]))  # []
print(dutch_flag_prob([0]))  # [0]
print(dutch_flag_prob([1]))  # [1]
print(dutch_flag_prob([2]))  # [2]


