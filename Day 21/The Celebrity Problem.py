"""A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people.  A square matrix mat is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

Examples:

Input: mat[][] = [[0 1 0],
                [0 0 0], 
                [0 1 0]]
Output: 1
Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity. 
Input: mat[][] = [[0 1],
                [1 0]]
Output: -1
Explanation: The two people at the party both know each other. None of them is a celebrity.
Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)

Constraints:
1 <= mat.size()<= 3000
0 <= mat[i][j]<= 1"""


class Solution:
    def celebrity(self, mat):
        n = len(mat)
        i, j = 0, n - 1
        
        while i < j:
            if mat[i][j] == 1:
                i += 1  # i knows j, so i can't be the celebrity
            else:
                j -= 1  # i doesn't know j, so j can't be the celebrity
        
        candidate = i
        
        for k in range(n):
            if k != candidate:
                if mat[candidate][k] == 1 or mat[k][candidate] == 0:
                    return -1
        
        return candidate