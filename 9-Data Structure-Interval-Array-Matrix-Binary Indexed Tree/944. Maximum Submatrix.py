# 944. Maximum Submatrix
# Given an n x n matrix of positive and negative integers, find the submatrix with the largest possible sum.

# Example
# Given matrix = 
# [
# [1,3,-1],
# [2,3,-2],
# [-1,-2,-3]
# ]
# return 9.
# Explanation:
# the submatrix with the largest possible sum is:
# [
# [1,3],
# [2,3]
# ]

class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return 0
        if matrix[0] is None or len(matrix[0]) == 0:
            return 0
        self.row = len(matrix)
        self.col = len(matrix[0])
        
        # prefix sum between row and row
        prefix_sum = self.getPrefixSum(matrix)
        max_sum = -sys.maxint
        
        for up in range(self.row):
            for down in range(up, self.row):
                arr = self.compression(matrix, up, down, prefix_sum)
                max_sum = max(max_sum, self.maximumSubarray(arr))
        return max_sum
    
    def getPrefixSum(self, matrix):
        sum_matrix = [[0 for i in range(self.col)] for j in range(self.row + 1)]

        for i in range(self.row):
            for j in range(self.col):
                sum_matrix[i+1][j] += sum_matrix[i][j] + matrix[i][j]
        return sum_matrix
    
    def compression(self, matrix, up, down, prefix_sum):
        arr = [0 for i in range(self.col)]
        for i in range(self.col):
            arr[i] = prefix_sum[down + 1][i] - prefix_sum[up][i]
        return arr
        
    def maximumSubarray(self, arr):
        temp_max = -sys.maxint
        temp_min = 0
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            if total < temp_min:
                temp_min = total
            if total - temp_min > temp_max:
                temp_max = total - temp_min
        return temp_max
        
