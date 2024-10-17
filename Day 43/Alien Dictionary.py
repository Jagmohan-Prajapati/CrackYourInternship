"""Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language. If no valid ordering of letters is possible, then return "".
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.

Examples :

Input:  n = 5, k = 4, dict = {"baa","abcd","abca","cab","cad"}
Output: 1
Explanation: Here order of characters is 'b', 'd', 'a', 'c' Note that words are sorted and in the given language "baa" comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.
Input: n = 3, k = 3, dict = {"caa","aaa","aab"}
Output: 1
Explanation: Here order of characters is 'c', 'a', 'b' Note that words are sorted and in the given language "caa" comes before "aaa", therefore 'c' is before 'a' in output.
Similarly we can find other orders.
Expected Time Complexity: O(n * |s| + k)
Expected Auxillary Space: O(k)

Constraints:
1 ≤ n≤ 104
1 ≤ k ≤ 26
1 ≤ Length of words ≤ 50"""


from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Create a graph
        adj = defaultdict(list)
        indegree = {chr(i + ord('a')): 0 for i in range(k)}

        # Build the graph
        for i in range(n - 1):
            word1, word2 = dict[i], dict[i + 1]
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    adj[c1].append(c2)
                    indegree[c2] += 1
                    break

        # Topological sort
        queue = deque([char for char in indegree if indegree[char] == 0])
        order = []
        
        while queue:
            char = queue.popleft()
            order.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != k:
            return ""
        
        return "".join(order)
