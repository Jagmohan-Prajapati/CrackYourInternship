"""Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1"""


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if max(max(grid)) == 0 or min(min(grid)) == 1: return -1
        ROWS, COLS = len(grid), len(grid[0])
        queue, visit = deque(), set()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r,c,0))
                    visit.add((r,c))
        res = 0
        while queue:
            r,c,dist = queue.popleft()
            for i, j in dirs:
                next_row = r + i
                next_col = c + j
                if 0 <= next_row < ROWS and 0 <= next_col < COLS and (next_row, next_col) not in visit:
                    new_dist = dist + 1
                    res = max(res, new_dist)
                    queue.append((next_row,next_col,new_dist))
                    visit.add((next_row,next_col))
        return res
        
            