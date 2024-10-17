"""You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1."""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        class UF:
            def __init__(self):
                self.sets = {}
                self.size = {}

            def find(self, i, j):
                if self.sets[(i, j)] == (i, j):
                    return (i, j)
                val = (i, j)
                p_i, p_j = self.sets[val]
                parent = self.find(p_i, p_j)
                self.sets[(i, j)] = parent
                return parent 

            def make_set(self, i, j):
                self.sets[(i, j)] = (i, j)

            def union(self, i1, j1, i2, j2):
                p1 = self.find(i1, j1)
                self.make_set(i2, j2)
                self.sets[(i2, j2)] = p1

            def update_size(self, i, j, size):
                i_p, j_p = self.find(i, j)
                self.size[(i_p, j_p)] = size

            def get_size(self, i, j):
                parent = self.find(i, j)
                return self.size[parent]
            
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = [[False for _ in range(n)] for _ in range(n)]
        uf = UF()

        def in_bounds(i, j):
            if 0 <= i < n and 0 <= j < n:
                return True
            return False

        def bfs(i, j):
            q = deque([(i, j)])
            comp_size = 0
            uf.make_set(i, j)
            vis[i][j] = True

            while len(q):
                c_i, c_j = q.popleft()
                uf.union(i, j, c_i, c_j)
                comp_size += 1
                for d_i, d_j in dirs:
                    new_i, new_j = c_i+d_i, c_j+d_j
                    if in_bounds(new_i, new_j) and not vis[new_i][new_j] and grid[new_i][new_j] == 1:
                        vis[new_i][new_j] = True
                        q.append((new_i, new_j))
            uf.update_size(i, j, comp_size)
            return comp_size
                        
 
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    # perform bfs, get the size of the component, asign the size to that set
                    # make all the components elements point to the element
                    comp_size = bfs(i, j)
                    if comp_size == n*n:
                        return n*n

        def handle_zero(i, j):
            max_union = 1 
            seen_components = set()

            for d_i, d_j in dirs:
                new_i, new_j = i + d_i, j + d_j

                if in_bounds(new_i, new_j) and grid[new_i][new_j] == 1:
                    parent = uf.find(new_i, new_j)
                    if parent not in seen_components:
                        seen_components.add(parent)
                        max_union += uf.get_size(new_i, new_j)

            return max_union

        max_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    max_island = max(max_island, handle_zero(i, j))
        return max_island