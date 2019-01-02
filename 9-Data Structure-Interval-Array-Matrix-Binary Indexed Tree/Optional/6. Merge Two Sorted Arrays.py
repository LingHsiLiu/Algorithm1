# 6. Merge Two Sorted Arrays
# Merge two given sorted integer array A and B into a new sorted integer array.

# Example
# A=[1,2,3,4]

# B=[2,4,5,6]

# return [1,2,2,3,4,4,5,6]

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        i, j  = 0, 0
        C = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        
        while i < len(A):
            C.append(A[i])
            i += 1
        while j < len(B):
            C.append(B[j])
            j += 1
        
        return C
