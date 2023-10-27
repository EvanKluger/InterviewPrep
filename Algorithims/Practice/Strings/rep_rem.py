def replace_and_remove(size, s):
    write_index, a_count = 0, 0

    for i in range(size):
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
        if s[i] == 'a':
            a_count +=1
    
    current_idx = write_index - 1
    write_index += a_count - 1

    while current_idx >= 0:
        if s[current_idx] == 'a':
            s[write_index-1:write_index+1] = 'dd'
            write_index -= 2
        else:
            s[write_index] = s[current_idx]
            write_index -= 1
        current_idx -= 1
    return s

s1 = ['a', 'c', 'd', 'b', 'b', 'c', 'a']
print(replace_and_remove(7, s1)) # Expected: ['d', 'd', 'c', 'd', 'd', 'c', 'd', 'd']

s2 = ['a', 'a']
print(replace_and_remove(2, s2)) # Expected: ['d', 'd', 'd', 'd']

s3 = ['b', 'b', 'b']
print(replace_and_remove(3, s3)) # Expected: []

s4 = ['a', 'b', 'a', 'b', 'a']
print(replace_and_remove(5, s4)) # Expected: ['d', 'd', 'd', 'd', 'd', 'd']

s5 = ['d', 'e', 'f']
print(replace_and_remove(3, s5)) # Expected: ['d', 'e', 'f']

    
    