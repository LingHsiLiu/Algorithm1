# 486. Merge K Sorted Arrays
# Given k sorted integer arrays, merge them into one sorted array.

# Example
# Given 3 sorted arrays:

# [
#   [1, 3, 5, 7],
#   [2, 4, 6],
#   [0, 8, 9, 10, 11]
# ]
# return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

# Challenge
# Do it in O(N log k).

# N is the total number of integers.
# k is the number of arrays.


import heapq #Priority Queue
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], index, 0))
        
        while len(heap):
            val, index, num = heap[0]
            heapq.heappop(heap)
        
            result.append(val)
            if num + 1 < len(arrays[index]):
                heapq.heappush(heap, (arrays[index][num+1], index, num + 1))
        return result
