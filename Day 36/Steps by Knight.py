"""Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.

Note:
The initial and the target position coordinates of Knight have been given according to 1-base indexing.

 

Example 1:

Input:
N=6
knightPos[ ] = {4, 5}
targetPos[ ] = {1, 1}
Output:
3
Explanation:

Knight takes 3 step to reach from 
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1).
 

 

Your Task:
You don't need to read input or print anything. Your task is to complete the function minStepToReachTarget() which takes the initial position of Knight (KnightPos), the target position of Knight (TargetPos), and the size of the chessboard (N) as input parameters and returns the minimum number of steps required by the knight to reach from its current position to the given target position or return -1 if its not possible.

 

Expected Time Complexity: O(N2).
Expected Auxiliary Space: O(N2).

 

Constraints:
1 <= N <= 1000
1 <= Knight_pos(X, Y), Targer_pos(X, Y) <= N"""


from collections import deque

class Solution:
    # Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        def is_inside(x, y):
            return 1 <= x <= N and 1 <= y <= N
        
        directions = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1)]
        queue = deque([(KnightPos[0], KnightPos[1], 0)])
        visited = set((KnightPos[0], KnightPos[1]))
        
        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == (TargetPos[0], TargetPos[1]):
                return steps
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_inside(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
                    
        return -1
