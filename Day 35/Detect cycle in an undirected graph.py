"""Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is connected.

Examples:

Input: V = 5, E = 5
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] 
Output: 1
Explanation: 

1->2->3->4->1 is a cycle.
 

Input: V = 4, E = 2
adj = [[], [2], [1, 3], [2]]
Output: 0
Explanation: 

No cycle in the graph.
 

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V) 

Constraints:
1 ≤ V, E ≤ 105"""


from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def dfs(v, parent):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False
