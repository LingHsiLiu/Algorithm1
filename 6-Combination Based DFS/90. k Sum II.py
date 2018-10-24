
# 90. k Sum II
# Given n unique integers, number k (1<=k<=n) and target.

# Find all possible k integers where their sum is target.

# Example
# Given [1,2,3,4], k = 2, target = 5. Return:

# [
#   [1,4],
#   [2,3]
# ]



class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        anslist = []
        self.dfs(A, k, target, 0, [], anslist)
        return anslist
    
    def dfs(self, A, k, target, index, onelist, anslist):
        if target == 0 and k == 0:
            anslist.append(onelist)
            return 
        if len(A) == index or target < 0 or k < 0:
            return 
        
        self.dfs(A, k, target, index + 1, onelist, anslist)
        self.dfs(A, k-1, target - A[index], index + 1, onelist + [A[index]], anslist)
