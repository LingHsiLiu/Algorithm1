# 16. Permutations II
# Given a list of numbers with duplicate number in it. Find all unique permutations.

# Example
# For numbers [1,2,2] the unique permutations are:

# [
#   [1,2,2],
#   [2,1,2],
#   [2,2,1]
# ]

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
        
        result = []
        result = self.permute(result, [], sorted(nums))
        return result
        
    def permute(self, result, temp, nums):
        if nums == []:
            result += [temp]
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.permute(result, temp+[nums[i]], nums[:i]+nums[i+1:])
        
        return result
        
