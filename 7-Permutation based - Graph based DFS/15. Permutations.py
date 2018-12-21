# 15. Permutations
# Given a list of numbers, return all possible permutations.

# Example
# For nums = [1,2,3], the permutations are:

# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        self.results = []
        self.dfs(nums, [])
        return self.results
        
    def dfs(self, nums, temp):
        
        if len(temp) == len(nums):
            self.results.append(temp[:])
            return
            
        for i in range(0, len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
                self.dfs(nums, temp)
                temp.pop()

