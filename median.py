
import random
import time
import tracemalloc
import math

def median_of_medians(arr):
    if len(arr) <= 5:#partionating the array into 5 sub arrays
        return sorted(arr)[len(arr) // 2]
    
    sublists = []
    i = 0
    while i < len(arr):
        # Slice out a sublist of 5 elements (or fewer if at the end)
        sublist = arr[i:i+5]
        sublists.append(sublist)
        i += 5
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    return median_of_medians(medians)

def deterministic(A, k):
    # print(f"{A} and {k}")
    left =[]
    middle =[]
    right =[]
    
    pivot = median_of_medians(A)

    for i in A:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        elif i > pivot:
            right.append(i)

    if k <= len(left):
        return deterministic(left, k)
    elif k<= len(left) + len(middle):
        return pivot
    else:
        return deterministic(right, k - len(left) - len(middle))

k = 3    

tracemalloc.start()
start = time.time()
sorted = deterministic(list(range(100)), k)
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for sorted numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))


# tracemalloc.start()
# start = time.time()
# deterministic(list(range(100, 0, -1)), k)
# end = time.time()
# current, peak_memory = tracemalloc.get_traced_memory()
# tracemalloc.clear_traces()
# print("Execution time for reverse sorted numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))


# tracemalloc.start()
# start = time.time()
# a = deterministic([random.randint(1, 500) for _ in range(10000)], k)
# # print("final", a)
# end = time.time()
# current, peak_memory = tracemalloc.get_traced_memory()
# tracemalloc.clear_traces()
# print("Execution time for random numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))




