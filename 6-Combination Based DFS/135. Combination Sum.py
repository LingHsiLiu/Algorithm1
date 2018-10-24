# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Example
# Given candidate set [2,3,6,7] and target 7, a solution set is:

# [7]
# [2, 2, 3]

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    # 數(candidates)可去多次
    
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results
        
    def dfs(self, candidates, target, start, combination, results):
        if target == 0:
            #deecopy
            return results.append(list(combination))
        
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            #[2] -> [2,2]
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            # self.dfs(candidates, target - candidates[i], i, combination + [candidates[i]])
            # [2,2] => [2]
            combination.pop() #backtracking
