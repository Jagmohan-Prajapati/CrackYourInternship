"""You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid."""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
 
        directions = [(0,1), (0,-1), (1,0), (-1,0)]  # right, left, up, down
        
        n = len(grid)
        m = len(grid[0])
        
        # find one point of a land
        def one_land(grid):
            for in_x, row in enumerate(grid):
                for in_y, val in enumerate(row):
                    if val:
                        return (in_x, in_y)
                    
        # start from one point and get all position of a land
        in_x, in_y = one_land(grid)
        queue = [(in_x, in_y)]
        first_land = [(in_x, in_y)]     # temp queue to find the first land
        
        from collections import defaultdict
        visited = defaultdict(lambda:False, {})
        visited[(in_x, in_y)] = True        
        
        # find positions of the first land
        while first_land:
            x, y = first_land.pop(0)
            for dir_x, dir_y in directions:
                nei_x = x + dir_x
                nei_y = y + dir_y
                if nei_x in range(n) and nei_y in range(m):       # point in range
                    if grid[nei_x][nei_y]:   # it is land
                        if not visited[(nei_x, nei_y)]:
                            first_land.append((nei_x, nei_y))
                            queue.append((nei_x, nei_y))
                            visited[(nei_x, nei_y)] = True
        
       
        
        # BFS
        cost = 0
        layer_size = 0
        while queue:
            layer_size = len(queue)
            for i in range(layer_size):
                x, y = queue.pop(0)
                for dir_x, dir_y in directions:
                    nei_x = x + dir_x
                    nei_y = y + dir_y
                    if nei_x in range(n) and nei_y in range(m):       # point in range
                        if not visited[(nei_x, nei_y)]:
                            if grid[nei_x][nei_y]:   # it is land (second land)
                                return cost
                            else:           # it is water
                                queue.append((nei_x, nei_y))
                                visited[(nei_x, nei_y)] = True
            cost += 1
        return None      