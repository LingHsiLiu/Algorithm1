# 545. Top k Largest Numbers II
# Implement a data structure, provide two interfaces:

# add(number). Add a new number in the data structure.
# topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.
# Example
# s = new Solution(3);
# >> create a new data structure.
# s.add(3)
# s.add(10)
# s.topk()
# >> return [10, 3]
# s.add(1000)

import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.k = k
        self.nums = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num): #logk
        # write your code here
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, num)
        elif num > self.nums[0]: #最小的top k值
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, num)

    """
    @return: Top k element
    """
    def topk(self):  #klogk
        # write your code here
        return sorted(self.nums, reverse=True)
