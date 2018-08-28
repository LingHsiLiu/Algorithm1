# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# Example
# Given nums = [2, 7, 11, 15], target = 9
# return [1, 2]

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        l = len(nums)
        if nums[0] + nums[l-1] == target:
            return (1, l)
        left, right = 0, l-1
        while left < right:
            while nums[left] + nums[right] > target and right > left:
                right -= 1
            if nums[left] + nums[right] == target:
                return (left + 1, right + 1)
            left +=1 
