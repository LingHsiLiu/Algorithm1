Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# Example
# Given s = "aab", return:

# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        results = []
        self.dfs(s, [], results)
        return results
    
    def dfs(self, s, stringlist, results):
        if len(s) == 0:
            results.append(stringlist)
            # results.append(list(stringlist))
            return
            
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                self.dfs(s[i:], stringlist + [prefix], results)
                # stringlist.append(prefix)
                # self.dfs(s[i:], stringlist, results)
                # stringlist.pop()

    def is_palindrome(self, s):
        return s == s[::-1]
