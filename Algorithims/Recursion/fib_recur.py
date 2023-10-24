def fib_recur(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recur(n-1) + fib_recur(n-2)

print(f'Fib 5 is {fib_recur(5)}') 
print(f'Fib 15 is {fib_recur(15)}') 
print(f'Fib 7 is {fib_recur(7)}') 