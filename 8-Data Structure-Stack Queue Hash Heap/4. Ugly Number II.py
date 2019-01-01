# 4. Ugly Number II
# Ugly number is a number that only have factors 2, 3 and 5.

# Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

# Example
# If n=9, return 10.

# Challenge
# O(n log n) or O(n) time.

# Notice
# Note that 1 is typically treated as an ugly number.

import heapq
class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        visited = set([1])

        val = None
        for i in range(n):
            val = heapq.heappop(heap) #O(n)取最小的數
            for multi in [2, 3, 5]:
                if val * multi not in visited:
                    visited.add(val * multi)
                    heapq.heappush(heap, val * multi)
        return val
