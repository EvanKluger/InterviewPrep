def radix_sort(arr):
    max_integer = 0

    for i in arr:
        max_integer = max(i, max_integer)
    
    num_digits = len(str(max_integer))

    for digit in num_digits:
        buckets = [[] for _ in range(10)]
        for number in arr:
            digit_value = (number // (10 ** digit)) % 10
            buckets[digit_value].append(number)

            arr = [number for bucket in buckets for number in bucket]

    return arr

    
    
