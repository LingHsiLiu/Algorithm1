# 547. Intersection of Two Arrays
# Given two arrays, write a function to compute their intersection.

# Example
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

# Challenge
# Can you implement it in three different algorithms?

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        
        # time: O(n+m)
        # extra space: O(m)
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        num_set = set(nums2)
        result_set = set()
        for num in nums1:
            if num in num_set:
                result_set.add(num)
        return list(result_set)
        
        # time: O(n+m)
        # extra space: O(n+m)
        
        # return list(set(nums1).intersection(set(nums2)))
        
        # extra space O(1)
        # extra memory O(1)
        # constant space
        # O(1) space
        # in place
        
        # extra -> no input, no output
        # 不包含輸入輸出
