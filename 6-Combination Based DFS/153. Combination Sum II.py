# 153. Combination Sum II
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Example
# Given candidate set [10,1,6,7,2,1,5] and target 8,

# A solution set is:

# [
#   [1,7],
#   [1,2,5],
#   [2,6],
#   [1,1,6]
# ]

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num.sort()        
        self.ans, tmp, use = [], [], [0] * len(num)        
        self.dfs(num, target, 0, 0, tmp, use)        
        return self.ans    
    def dfs(self, can, target, p, now, tmp, use):        
        if now == target:            
            self.ans.append(tmp[:])            
            return        
        for i in range(p, len(can)):            
            if now + can[i] <= target and (i == 0 or can[i] != can[i-1] or use[i-1] == 1):                
                tmp.append(can[i])
                use[i] = 1                
                self.dfs(can, target, i+1, now + can[i], tmp, use)                
                tmp.pop()                
                use[i] = 0
                
