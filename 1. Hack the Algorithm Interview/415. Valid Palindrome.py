# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example
# "A man, a plan, a canal: Panama" is a palindrome.

# "race a car" is not a palindrome.

# Challenge
# O(n) time without extra memory.

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here

        start = 0
        end = len(s)-1
        
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start +=1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -=1  
            if start < end and s[start].lower() != s[end].lower():
                return False

            start += 1
            end -=1
        return True
