"""The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix. mat[i][j] denotes the weight of the edge from i to j. If mat[i][j] = -1, it means there is no edge from i to j.
Note: Modify the distances for every pair in place.

Examples :

Input: mat = [[0, 25], [-1, 0]]

Output: [[0, 25], [-1, 0]]

Explanation: The shortest distance between every pair is already given(if it exists).
Input: mat = [[0, 1, 43],[1, 0, 6], [-1, -1, 0]]

Output: [[0, 1, 7], [1, 0, 6], [-1, -1, 0]]

Explanation: We can reach 2 from 0 as 0->1->2 and the cost will be 1+6=7 which is less than 43.
Constraints:
1 <= mat.size() <= 100
-1 <= mat[ i ][ j ] <= 1000"""


from typing import List

class Solution:
    def shortest_distance(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        
        # Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if mat[i][j] != -1:
                    dist[i][j] = mat[i][j]
                if i == j:
                    dist[i][j] = 0

        # Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Update the original matrix with shortest distances
        for i in range(n):
            for j in range(n):
                if dist[i][j] == float('inf'):
                    mat[i][j] = -1
                else:
                    mat[i][j] = dist[i][j]
        
        return mat
