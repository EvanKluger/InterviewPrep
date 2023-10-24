def fac_recur(n):
    if n <= 1:
        return 1  
    return n * fac_recur(n-1)

print(f'Fac 5 is {fac_recur(5)}') 