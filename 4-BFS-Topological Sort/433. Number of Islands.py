from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    print(grid[i][j])
                    self.bfs(grid, i, j)
                    islands += 1
        
        return islands
    
    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        # print(queue)
        grid[x][y] = False ## 訪問過設為0 
        while queue:
            # print(queue)
            x, y = queue.popleft() # take all tuple from left
            print(x, y)
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]: ##下左上右
                next_x = x + delta_x
                next_y = y + delta_y
                # print(delta_x, delta_y)
                if not self.is_valid(grid, next_x, next_y):
                    continue ## 回到for delta_x......
                queue.append((next_x, next_y))
                grid[next_x][next_y] = False ## 訪問過設為0 
    
    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y]
