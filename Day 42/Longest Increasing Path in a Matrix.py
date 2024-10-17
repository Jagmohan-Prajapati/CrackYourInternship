"""Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1"""

class Solution:

    def solve(self, i, j, matrix, m, n, dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        ans = 0

        # up
        if (i-1>=0 and matrix[i][j]<matrix[i-1][j]):
            ans = max(ans, self.solve(i-1, j, matrix, m, n, dp))
        # right
        if(j+1<n and matrix[i][j]<matrix[i][j+1]):
            ans = max(ans, self.solve(i, j+1, matrix, m, n, dp))
        # down
        if(i+1<m and matrix[i][j]<matrix[i+1][j]):
            ans = max(ans, self.solve(i+1, j, matrix, m, n, dp))
        # left
        if(j-1>=0 and matrix[i][j]<matrix[i][j-1]):
            ans = max(ans, self.solve(i, j-1, matrix, m, n, dp))
        
        dp[i][j] = ans+1
        return dp[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -1
        dp = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.solve(i, j, matrix, m, n, dp))
        return ans