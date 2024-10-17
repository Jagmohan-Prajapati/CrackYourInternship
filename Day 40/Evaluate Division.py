"""You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits."""



class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. Build graph:
        graph = {}   # the graph is saved like this: node.val:[neighbors], where neighbors is a list of lists [neighbor.val, edge_value]
        graph = {}
        for i, (v1, v2) in enumerate(equations):
            div = values[i]
            if v1 not in graph:
                graph[v1] = []
            if v2 not in graph:
                graph[v2] = []
            graph[v1].append([v2, div])
            graph[v2].append([v1, 1/div])
        
        
        # 2. compute_path function, to get the total value along the graph
        def compute_path(a,b):
            visited = set()
            path = []
            q = deque()
            q.append([a, 1])

            while q:
                curr_node, curr_val = q.popleft()
                if curr_node in visited:
                    continue
                visited.add(curr_node)
                neighbors = graph[curr_node]
                for x, val in neighbors:
                    if x == b:
                        return curr_val * val
                    else:
                        q.append([x, curr_val * val])
        
            return -1


        # 3. prepare the result 
        res = []
        for v1, v2 in queries:
            if v1 not in graph or v2 not in graph:
                res.append(-1)
            elif v1 == v2:
                res.append(1)
            else:
                res.append( compute_path(v1, v2) )   # path = [2, 4, 5] (edge values) or path = -1 (no path )


        return res
