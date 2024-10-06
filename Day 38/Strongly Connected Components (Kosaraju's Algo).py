
"""Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.
 

Example 1:

Input:

Output:
3
Explanation:

We can clearly see that there are 3 Strongly
Connected Components in the Graph
Example 2:

Input:

Output:
1
Explanation:
All of the nodes are connected to each other.
So, there's only one SCC.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function kosaraju() which takes the number of vertices V and adjacency list of the graph of size V as inputs and returns an integer denoting the number of strongly connected components in the given graph.
 

Expected Time Complexity: O(V+E).
Expected Auxiliary Space: O(V+E).
 

Constraints:
1 ≤ V ≤ 5000
0 ≤ E ≤ (V*(V-1))
0 ≤ u, v ≤ V-1
Sum of E over all testcases will not exceed 25*106"""


from typing import List

class Solution:
    # Function to find number of strongly connected components in the graph.
    def kosaraju(self, V: int, adj: List[List[int]]) -> int:
        def dfs(v, visited, stack):
            visited[v] = True
            for neighbour in adj[v]:
                if not visited[neighbour]:
                    dfs(neighbour, visited, stack)
            stack.append(v)
        
        def reverse_graph(V, adj):
            rev_adj = [[] for _ in range(V)]
            for i in range(V):
                for j in adj[i]:
                    rev_adj[j].append(i)
            return rev_adj
        
        def dfs_reversed(v, visited, rev_adj):
            visited[v] = True
            for neighbour in rev_adj[v]:
                if not visited[neighbour]:
                    dfs_reversed(neighbour, visited, rev_adj)
        
        # Step 1: Perform DFS and push nodes to stack on finish time
        stack = []
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                dfs(i, visited, stack)
        
        # Step 2: Reverse the graph
        rev_adj = reverse_graph(V, adj)
        
        # Step 3: Perform DFS based on vertex finishing order in original graph
        visited = [False] * V
        scc_count = 0
        while stack:
            v = stack.pop()
            if not visited[v]:
                dfs_reversed(v, visited, rev_adj)
                scc_count += 1
        
        return scc_count
