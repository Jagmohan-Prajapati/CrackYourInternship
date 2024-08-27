"""Given a Linked List, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked lists is in sorted order.
Flatten the Link List so all the nodes appear in a single level while maintaining the sorted order.

Note: The flattened list will be printed using the bottom pointer instead of the next pointer. Look at the printList() function in the driver code for more clarity.

Examples:
Input:

Output:  5-> 7-> 8- > 10 -> 19-> 20-> 22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation: The resultant linked lists has every node in a single level.(Note: | represents the bottom pointer.)

Input:
 
Output: 5-> 7-> 8-> 10-> 19-> 22-> 28-> 30-> 50
Explanation: The resultant linked lists has every node in a single level.(Note: | represents the bottom pointer.)

Note: In the output section of the above examples, the -> represents the bottom pointer.

Expected Time Complexity: O(n * n * m)
Expected Auxiliary Space: O(n)

Constraints:
0 <= number of nodes <= 50
1 <= no. of nodes in sub-LinkesList(mi) <= 20
1 <= node->data <= 103"""

'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        def mergeTwoLists(a, b):
            if a is None: return b
            if b is None: return a
            if a.data < b.data:
                a.bottom = mergeTwoLists(a.bottom, b)
                a.next = None
                return a
            else:
                b.bottom = mergeTwoLists(a, b.bottom)
                b.next = None
                return b
        
        if root is None or root.next is None:
            return root
        
        root.next = self.flatten(root.next)
        root = mergeTwoLists(root, root.next)
        
        return root