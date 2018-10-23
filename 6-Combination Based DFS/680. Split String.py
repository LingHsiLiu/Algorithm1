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
    # 先12 => "1", "2", "12"
    # 再加3
    
    def splitString(self, s):
        # write your code here
        return self.helper(s)
        
    def helper(self, s):
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        
        rt = []
        one = self.splitString(s[:-1])
        two = self.splitString(s[:-2])
#         print(one)
#         print(two)
        
        for o in one:
            rt.append(o + [s[-1]])
            
        for t in two:
            rt.append(t + [s[-2:]])
            
        return rt
