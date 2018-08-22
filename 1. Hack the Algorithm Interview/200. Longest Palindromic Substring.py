# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# Example
# Given the string = "abcdzdcab", return "cdzdc".

# Challenge
# O(n2) time is acceptable. Can you do it in O(n) time.

class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""
            
        longest = ""
        for middle in range(len(s)):
            sub = self.find_palindrome_from(s, middle, middle)
            if len(sub) > len(longest):
                longest = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub
            
        return longest
            
    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1 
            right += 1
        return string[left + 1 : right]

        
