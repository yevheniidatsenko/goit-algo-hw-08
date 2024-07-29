## Heaps or Pyramids

Welcome to the homework on the topic "Heaps"! 🙂

In this topic, you will learn about heaps, a specialized tree-based data structure that maintains a specific order property. Heaps are used to implement priority queues, enabling efficient access to the highest (or lowest) priority element. You also explored heap sort, an efficient sorting algorithm that utilizes the heap structure. The `heapq` module in Python provides tools to work with heaps.

## Description of Tasks

### Task 1: Minimum Cost to Connect Ropes

Imagine that you are given the following problem to solve during a technical interview, using heaps.

You have several network cables of different lengths. You need to connect them two at a time into one cable using connectors, in an order that results in the least cost. The cost of connecting two cables is equal to the sum of their lengths, and the total cost is the sum of connecting all cables.

The task is to find the order of connections that minimizes the total cost.

### Task 2 (Optional): Merge k Sorted Lists

Given `k` sorted lists of integers, your task is to merge them into one sorted list. For this task, you should use a min-heap to efficiently merge multiple sorted lists into one sorted list. Implement the function `merge_k_lists` which takes a list of sorted lists as input and returns a sorted list.

#### Example:

```python
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Merged list:", merged_list)
```

#### Expected Output:

```
Merged list: [1, 1, 2, 3, 4, 4, 5, 6]
```
