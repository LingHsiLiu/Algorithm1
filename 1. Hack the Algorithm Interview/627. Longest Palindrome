  # Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

  # This is case sensitive, for example "Aa" is not considered a palindrome here.

  # Example
  # Given s = "abccccdd" return 7

  # One longest palindrome that can be built is "dccaccd", whose length is 7.

  # Notice
  # Assume the length of given string will not exceed 1010.
  
  class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        hash = {}
        for i in s:
            if i in hash:
                del hash[i]
            else:
                hash[i] = True
        
        remove = len(hash)
        if remove > 0:
            remove = remove - 1
        return len(s) - remove
