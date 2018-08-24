# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# Example
# Given [4, 5, 6, 7, 0, 1, 2] return 0

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if nums is None:
            return -1
        start = 0
        end = len(nums) -1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[end] < nums[mid]:  ##先判斷end
                start = mid
            else:
                end = mid 
        return min(nums[start], nums[end])
