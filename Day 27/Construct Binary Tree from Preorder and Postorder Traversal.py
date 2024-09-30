"""Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0: return None
        elif len(preorder)==1: return TreeNode(val=preorder[0])
        else:
            root=preorder.pop(0)
            postorder.pop()
            preleft=preorder[:preorder.index(postorder[-1])]
            preright=preorder[preorder.index(postorder[-1]):]
            postleft=postorder[:postorder.index(preorder[0])+1]
            postright=postorder[postorder.index(preorder[0])+1:]
            if preorder[0]==postorder[-1]: preleft,preright=preright,preleft
            return TreeNode(
                val=root,
                left=self.constructFromPrePost(preleft,postleft),
                right=self.constructFromPrePost(preright,postright)
            )