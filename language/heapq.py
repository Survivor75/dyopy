"""
Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
"""
from heapq import heapify, heappush, heappop, heapreplace, heappushpop, nlargest, nsmallest


def main():
    A = [10, 2, 9, 4, 7, 6, 5, 8, 3, 1]

    """
    Transform list A into a heap, in-place, in linear time.
    """
    heapify(A)

    """
    Push the value item onto the heap, maintaining the heap invariant.
    """
    heappush(A, 11)

    """
    Pop and return the smallest item from the heap, maintaining the heap invariant. 
    If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
    """
    heappop(A)

    """
    Push item on the heap, then pop and return the smallest item from the heap. 
    The combined action runs more efficiently than heappush() followed by a separate call to heappop().
    """
    heappushpop(A, 1)

    """
    Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. 
    If the heap is empty, IndexError is raised. The value returned may be larger than the item added. 
    If that isn’t desired, consider using heappushpop() instead. 
    Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.
    """
    heapreplace(A, 15)

    """
    Return a list with the n largest elements from the dataset defined by iterable. 
    """
    nlargest(3, A, key=lambda x: x > 3)

    """
    Return a list with the n smallest elements from the dataset defined by iterable.
    """
    nsmallest(3, A, key=lambda x: x < 3)


if __name__ == '__main__':
    main()
