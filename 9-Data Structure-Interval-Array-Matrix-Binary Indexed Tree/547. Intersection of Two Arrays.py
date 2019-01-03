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
        return list(set(nums1).intersection(set(nums2)))
