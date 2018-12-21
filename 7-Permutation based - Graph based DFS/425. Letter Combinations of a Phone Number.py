# 425. Letter Combinations of a Phone Number
# Given a digit string excluded 01, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Example
# Given "23"

# Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#時間複雜度 3^N ～ 4^N 之間
KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    
    # '2': ['a','b','c'],
    # '3': ['d','e','f'],
    # '4': ['g','h','i'],
    # '5': ['j','k','l'],
    # '6': ['m','n','o'],
    # '7': ['p','q','r','s'],
    # '8': ['t','u','v'],
    # '9': ['w','x','y','z'],
}

# String[] KEYBOARD = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        results = []
        self.dfs(digits, 0, '', results)
        
        return results
    
    def dfs(self, digits, index, string, results):
        if index == len(digits):
            print(index)
            results.append(string)
            print(results)
            return
        
        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + letter, results)
