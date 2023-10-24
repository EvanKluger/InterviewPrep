import sys
sys.path.append("../../")

from Data_Structures.heap import Heap

def heap_sort(arr):
    heap = Heap()

    for val in arr:
        heap.insert(val)
    
    sorted_arr = []

    while heap.is_empty() == False:
        sorted_arr.append(heap.extract_min())
    
    return sorted_arr

    
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = heap_sort(arr)
print(sorted_arr)

