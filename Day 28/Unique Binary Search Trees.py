"""Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19"""

class Solution:
    def numTrees(self, n: int) -> int:
        self.table = [-1] * (n+1)
        self.table[0] = 1
        return self.numTreesRec(n)
        
    def numTreesRec(self, n):
        if self.table[n] != -1:
            return self.table[n]
        total = 0
        for m in range(n):
            total += (self.numTreesRec(n-1-m) * self.numTreesRec(m))
        self.table[n] = total
        return total