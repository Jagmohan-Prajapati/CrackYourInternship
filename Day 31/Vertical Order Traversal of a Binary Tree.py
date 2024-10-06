"""Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.vot = {}
        self.find(root)
        self.vot = sorted(self.vot.items(),key=cmp_to_key(Compare.main))
        mapp = {}
		# final merge
        for key,value in self.vot:
            mapp[key[-1]] = mapp.get(key[-1],[]) + value
        return list(mapp.values())
    
    
    def find(self,root,x=0,y=0):
		# traversing the root node to get all (x,y) pairs with node values
        if root == None:
            return
        self.vot[(x,y)] = self.insert(self.vot.get((x,y),[]),root.val)
        self.find(root.left,x+1,y-1)
        self.find(root.right,x+1,y+1)
        
        
    def insert(self, arr, elm):
		# function for inserting a value in our map that have same (x,y) while traversing 
        if not arr:
            return [elm]
        for index,curr in enumerate(arr):
            if curr >= elm:
                return arr[:index] + [elm] + arr[index:]
        return arr + [elm]

class Compare:
    def main(self,elm):
		# comparing the position of y
        if self[0][-1]<elm[0][-1]:
            return -1
        elif self[0][-1]>elm[0][-1]:
            return 1
        else:
			# if position of y is same for both self and elm, compare the position of x -1 represents for smaller and 1 represents for larger
            if self[0][0]<elm[0][0]:
                return -1
            else:
                return 1