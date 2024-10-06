"""There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree."""

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        return sum_impl(n, edges)

def dfs_subtree_size(tree, u, subtree_size, depth):
    k = 1
    val = depth[u] + 1
    for v in tree[u]:
        if depth[v] is None:
            depth[v] = val
            k += dfs_subtree_size(tree, v, subtree_size, depth)
    subtree_size[u] = k
    return k

def dfs_sum(tree, u, d_subtree, dist):
    val = dist[u] + len(tree)
    for v in tree[u]:
        if dist[v] is None:
            dist[v] = val - 2 * d_subtree[v]
            dfs_sum(tree, v, d_subtree, dist)

def sum_impl(n, edges):
    assert len(edges) == n - 1
    if not edges:
        return [0]
    tree = [list() for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    subtree_size = [None] * n
    depth = [None] * n
    depth[0] = 0
    dfs_subtree_size(tree, 0, subtree_size, depth)
    dist = [None] * n
    dist[0] = sum(depth)
    dfs_sum(tree, 0, subtree_size, dist)
    return dist