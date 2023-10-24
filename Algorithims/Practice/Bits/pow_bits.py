#Compute the power of a n

def pow_bits(x,y):
    result = 1

    while y != 0:
        if y & 1 == 1:
            result *= x
        x = x*x
        y >>= 1
    return result


five = pow_bits(5,3)
six = pow_bits(6,4)
seven = pow_bits(7,20)
eight = pow_bits(8,1)

print(f'five^3 is : {five}')
print(f'six^4 is: {six}')
print(f'seven^20 is: {seven}')
print(f'eight^1 is: {eight}')