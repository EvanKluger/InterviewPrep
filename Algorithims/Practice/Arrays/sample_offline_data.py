#sample offline data
#implment algo to take in array of distinct elements and size and return a subset of the given size of the array elements

import random

def random_sampling(k, arr):
    n = len(arr)

    for i in range(k):
        j = random.randint(i, n-1)

        arr[i], arr[j] = arr[j], arr[i]

    return arr[:k]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random_sampling(3, arr))
print(random_sampling(5, arr))