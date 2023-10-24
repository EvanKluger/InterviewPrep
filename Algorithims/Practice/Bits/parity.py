
#Find whether a number is even or odd based on bits

def parity(n):
    n_bit = bin(n)
    if n_bit[-1] == '0':
        return True
    else:
        return False
    
five = parity(5)
six = parity(6)
seven = parity(7)
eight = parity(8)

print(f'five is an even: {five}')
print(f'six is an even: {six}')
print(f'seven is an even: {seven}')
print(f'eight is an even: {eight}')

def parity2(word):
    result = 0
    while word:
        result ^= word & 1
        word >>= 1
    return result
