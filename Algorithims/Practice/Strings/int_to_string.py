#Int to String

def int_to_string(x):
    is_neg = False
    if x < 0:
        is_neg = True
        x = -x
    
    if x == 0:
        return '0'
    
    result = []

    while x > 0:    
        result.append(chr(ord('0') + x % 10))
        x //= 10
    

    ans = ''.join(result[::-1])
    
    if is_neg:
        return '-' + ans
    else:
        return ans

print(int_to_string(123))  # Expected output: "123"
print(int_to_string(1))    # Expected output: "1"
print(int_to_string(98765))# Expected output: "98765"
print(int_to_string(1000000000))   # Expected output: "1000000000"
print(int_to_string(-1000000000))  # Expected output: "-1000000000"
print(int_to_string(0))    # Expected output: "0"



    
    