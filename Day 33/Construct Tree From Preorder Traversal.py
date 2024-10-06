"""Given a binary tree. Find the size of its largest subtree which is a Binary Search Tree.
Note: Here Size equals the number of nodes in the subtree.

Examples :

Input:   1
        /  \
        4   4              
       / \ 
      6   8
Output: 1 
Explanation: There's no sub-tree with size greater than 1 which forms a BST. All the leaf Nodes are the BSTs with size equal to 1.

Input:    6
        /   \
      6      2              
       \    / \
        2  1   3
Output: 3
Explanation: The following sub-tree is a BST of size 3:  2
                                                       /   \
                                                      1     3
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 106"""

class Solution:
    def largestBst(self, root):
        def helper(node):
            if node is None:
                return (True, 0, float('inf'), float('-inf'))
            
            left_is_bst, left_size, left_min, left_max = helper(node.left)
            right_is_bst, right_size, right_min, right_max = helper(node.right)
            
            if left_is_bst and right_is_bst and left_max < node.data < right_min:
                size = left_size + right_size + 1
                return (True, size, min(left_min, node.data), max(right_max, node.data))
            
            return (False, max(left_size, right_size), 0, 0)
        
        return helper(root)[1]