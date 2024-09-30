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

The time complexity of the array when inserting an element is O(1). However, the time complexity can be O(n) when resizing is required when ints are inserted or deleted except for the last element. The time complexity of the matrix is O(n *m), where m is the number of rows and n is the number of elements in the array. The time complexity for stack, queue, or the linked list is O(1) when simply inserting elements. Stack and queues can have the time complexity of O(n) when a delete operation or a search is done from the dataset. For the linked list, the time complexity for adding an element or deleting a certain element is O(n) since it has to traverse from head to tail to find the correct value. Arrays can be useful for creating a stack or a queue when there is only reading is involved which will better time complexity but when the forst element is deleted a whole arrays has to shift left which can be inefficient for memory. However, building it from a LinkedList can have some advantages since removing the first or last item can be very easy, can have the time complexity of O(1), and does not require moving or shifting the nodes since they are linked with a pointer in the nodes. Hence, the data structure is very efficient and can be used in various everyday scenarios. Array lists or arrays can be very helpful if the data is only for reading, which is realistic most of the time, like getting information from the database. Similarly, a linked list would be for those where a value needs to be added or deleted frequently since it does not have to shift the nodes as they are linked with the pointers. The different kinds of list list implementation are very advantageous in real-world applications.

