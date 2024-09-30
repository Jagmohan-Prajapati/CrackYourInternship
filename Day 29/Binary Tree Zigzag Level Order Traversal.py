"""Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        level = 0
        ans = []
        queue = deque()
        queue.append(root)

        #print(queue)

        while queue:
            curr_len = len(queue)
            curr_queue = deque()

            for i in range(curr_len):
                curr = queue.popleft()
                #print(curr)
                if level % 2 == 0:
                    curr_queue.append(curr.val)
                else:
                    curr_queue.appendleft(curr.val)
            
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            ans.append(list(curr_queue))
            level += 1
        
            #print(ans)
        
        return ans