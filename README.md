# How to run

```
python3 ./median.py
python3 ./quickSelect.py
```

The medians of medians algorithm is a deterministic algorithm that can be used to find the kth smallest element in an array without sorting a whole array. Using a straightforward implementation, we usually sort an array, which could take the time complexity of O(nlogn), and then we can get the index of k-1 to get the kth element from the array. With the medians of medians algorithm, we can achieve the goal with O(n) in the worst case. We divide the array into 5 subarrays and sort each group, which takes constant time, and then find the median of each group. Then it is used to calculate medians of the median to find the pivot for partitioning with data smaller and larger than the pivot. Then, it is recursively traversed through each group. If the larger group is bigger, then recursed through the larger group or traversed through the small group to get the the largest element. The operation can be achieved by using quixkselect which is the small modification of QuickSort.It has a time complexity of O(n); however, the worst case of quick select is O(n^2). This happens when the input dataset is sorted in order or partially sorted, and every time, it has to swap the element. But on overage, it will have the time complexity of O(n). And from the analysis with sorted, reverse sorted and random elemnts, medians of medians performed better when calculating the kth element.


# How To

```
python3 ./arrays.py
python3 ./matrices.py
python3 ./stack.py
python3 ./queues.py
python3 ./linkedList.py
```




