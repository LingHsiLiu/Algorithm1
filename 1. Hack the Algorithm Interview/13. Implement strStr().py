# For a given source string and a target string, you should output the first index(from 0) of target string in source string.

# If target does not exist in source, just return -1.

# Example
# If source = "source" and target = "target", return -1.

# If source = "abcdabcdefg" and target = "bcd", return 1.


class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while (j < len_t):
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1
