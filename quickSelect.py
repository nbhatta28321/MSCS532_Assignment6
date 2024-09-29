
import random
import time
import tracemalloc

def partition(A, l, r): #
    
    x = r
    i = l
    for j in range(l, r):
        
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
            
    A[i], A[r] = A[r], A[i]
    return i

def getElement(A, left, right, k):

    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= right - left + 1):

        # index of the pivot 
        index = partition(A, left, right)

        # if position is same as k
        if (index - left == k - 1):
            return A[index]

        # if exdex is left of k then recursively iterate to left arr
        if (index - left > k - 1):
            return getElement(A, left, index - 1, k)

        # Else towards the right 
        return getElement(A, index + 1, right, k - index + left - 1)

def quickSelect(A, k):
    # print(f"{A} and {k}")
    return getElement(A, 0, len(A)-1, k)

k = 3    
tracemalloc.start()
start = time.time()
sorted = quickSelect(list(range(100)), k)
# print("final", sorted)

end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for sorted numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))


tracemalloc.start()
start = time.time()
quickSelect(list(range(100, 0, -1)), k)
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for reverse sorted numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))


tracemalloc.start()
start = time.time()
a = quickSelect([random.randint(1, 77) for _ in range(100)], k)
# print("final", a)
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for random numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))
