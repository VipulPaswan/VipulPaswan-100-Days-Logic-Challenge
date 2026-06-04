📘 Day 18 – Priority Queue (Min Heap)

A Priority Queue processes elements based on priority instead of order.
Lower number → higher priority.

Why Min Heap?

Min Heap keeps the smallest priority value at the top.
This makes operations efficient:

Insert: O(log n)

Remove min: O(log n)

Peek: O(1)

What I Implemented

MinHeap class (bubbleUp, sinkDown, insert, extractMin)

PriorityQueue class (enqueue, dequeue, peek, size, isEmpty)

Example Output

Tasks processed in correct priority order:
1 → 3 → 4 → 5 → 6 → 7

Key Takeaway

Priority Queue + Min Heap = fast scheduling system used in OS, networking, and pathfinding algorithms.
