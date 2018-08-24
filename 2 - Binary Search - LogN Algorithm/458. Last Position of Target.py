# Find the last position of a target number in a sorted array. Return -1 if target does not exist.

# Example
# Given [1, 2, 2, 4, 5, 5].

# For target = 2, return 2.

# For target = 5, return 5.

# For target = 6, return -1.


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums or target is None:
            return -1
        start = 0
        end = len(nums) -1
        
        while start + 1 < target: ### 避免死循環
            mid = start + (end - start) // 2 ##整除
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid
            else:
                start = mid
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        else: 
            return -1
