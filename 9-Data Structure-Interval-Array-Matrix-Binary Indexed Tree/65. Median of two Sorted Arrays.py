# 65. Median of two Sorted Arrays
# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

# Example
# Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

# Given A=[1,2,3] and B=[4,5], the median is 3.

# Challenge
# The overall run time complexity should be O(log (m+n)).

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    # O(log (m+n))
    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findkth(A, B, n/2 + 1)
        else:
            smaller = self.findkth(A, B, n/2)
            bigger = self.findkth(A, B, n/2 + 1)
            return (smaller + bigger) / 2.0
        
    def findkth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        
        a = A[k / 2 - 1] if len(A) >= k / 2 else None
        b = B[k / 2 - 1] if len(B) >= k / 2 else None
        
        if b is None or (a is not None and a < b):
            return self.findkth(A[k / 2:], B, k - k / 2)
        return self.findkth(A, B[k / 2:], k - k / 2)
        
