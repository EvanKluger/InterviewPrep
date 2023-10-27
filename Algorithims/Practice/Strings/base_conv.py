
def base_conv(s, b1, b2):
    
    def char_to_num(char):
        if '0' <= char <= '9':
            return int(char)
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 10
    
    def num_to_char(num):
        if 0 <= num <= 9:
            return str(num)
        elif 10 <= num <= 35:
            return chr(num - 10 + ord('A'))
    
    decimal_val = 0
    for idx, char in enumerate(reversed(s)):
        decimal_val += char_to_num(char) * (b1 ** idx)

    
    result = []
    while decimal_val > 0:
        remainder = decimal_val % b2
        result.append(num_to_char(remainder))
        decimal_val //= b2
        # use modulo operation to get the remainder
        # handle characters and digits for base `b2`
        # update the result list
    
    return ''.join(result[::-1])

print(base_conv("A1", 16, 10))  # 161 in base 10
print(base_conv("1010", 2, 10)) # 10 in base 10
print(base_conv("10", 10, 2))   # 1010 in base 2
print(base_conv("161", 10, 16)) # A1 in base 16