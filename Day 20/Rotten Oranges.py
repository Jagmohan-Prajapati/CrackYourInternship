"""Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
 

Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and 
(2,1) in unit time.
Example 2:

Input: grid = {{2,2,0,1}}
Output: -1
Explanation: The grid is-
2 2 0 1
Oranges at (0,0) and (0,1) can't rot orange at
(0,3).
 

Your Task:
You don't need to read or print anything, Your task is to complete the function orangesRotting() which takes grid as input parameter and returns the minimum time to rot all the fresh oranges. If not possible returns -1.
 

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
 

Constraints:
1 ≤ n, m ≤ 500"""

class Solution:
    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        time_elapsed = 0
    
        # Initialize the queue with all rotten oranges and count the fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
    
        # If there are no fresh oranges, return 0 (no time needed)
        if fresh_count == 0:
            return 0
    
        # Directions for the adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
        # BFS to rot the adjacent oranges
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Rot the fresh orange
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            time_elapsed += 1
    
        # If there are still fresh oranges left, return -1
        if fresh_count > 0:
            return -1
    
        # Subtract 1 from time_elapsed because the last increment happens after the last orange rots
        return time_elapsed - 1