# 654. Sparse Matrix Multiplication
# Given two Sparse Matrix A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

# Example
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]


#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        n = len(A) # row
        m = len(A[0]) # col
        k = len(B[0]) # col
        
        C = [[0 for _ in xrange(k)] for i in xrange(n)]
        # print(C)

        for i in xrange(n):
            for j in xrange(m):
                if A[i][j] != 0:
                    for l in xrange(k):
                        C[i][l] += A[i][j] * B[j][l]
        return C
        

