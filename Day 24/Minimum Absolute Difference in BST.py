"""Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def inorder(troot):
            nonlocal arr
            if not troot:
                return
            inorder(troot.left)
            arr.append(troot.val)
            inorder(troot.right)
        inorder(root)
        x=float("inf")
        for i in range(1,len(arr)):
            x=min(arr[i]-arr[i-1],x)
        return x