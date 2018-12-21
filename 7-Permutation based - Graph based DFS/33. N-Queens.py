# 33. N-Queens
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example
# There exist two distinct solutions to the 4-queens puzzle:

# [
#   // Solution 1
#   [".Q..",
#   "...Q",
#   "Q...",
#   "..Q."
#   ],
#   // Solution 2
#   ["..Q.",
#   "Q...",
#   "...Q",
#   ".Q.."
#   ]
# ]

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        results = []
        self.search(n, [], results)
        return results
        
    def search(self, n, cols, results):
        row = len(cols)
        if row == n:
            results.append(self.draw_chessboard(cols))
            return

        for col in range(n):
            if not self.is_valid(cols, row, col):
                continue
            cols.append(col)
            self.search(n, cols, results)
            cols.pop()
            
    def draw_chessboard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
        
    def is_valid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
        return True
