# 680. Split String
# Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

# Example
# Given the string "123"
# return [["1","2","3"],["12","3"],["1","23"]]

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        result = []
        self.dfs(result, [], s)
        return result

    def dfs(self, result, path, s):
        if s =="":
            result.append(path[:])
            return
        for i in range(2):
            if i+1 <= len(s):
                path.append(s[i+1])
                self.dfs(rsult, path, s[i+1:])
                path.pop()
