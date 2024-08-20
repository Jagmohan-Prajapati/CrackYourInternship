"""Given a singly linked list, remove all the nodes with any node on their right whose value is greater and return the head of the modified linked list.  (Not just the immediate Right, but the entire List on the Right)

Examples:
Input:
LinkedList = 12->15->10->11->5->6->2->3
Output: 15 11 6 3

Explanation: Since, 12, 10, 5 and 2 are the elements which have greater elements on the following nodes. So, after deleting them, the linked list would like be 15, 11, 6, 3.

Input:
LinkedList = 10->20->30->40->50->60
Output: 60
Explanation: All the nodes except the last node has a greater value node on its right, so all the nodes except the last node must be removed.

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
1 ≤ size of linked list ≤ 105
1 ≤ element of linked list ≤ 105

Note: Try to solve the problem without using any extra space."""


class Node:
    def __init__(self,x):
        self.data=x
        self.next=None


class Solution:
    def compute(self,head):
        head = self.reverseList(head)
        max_node = head
        curr = head

        while curr and curr.next:
            if curr.next.data < max_node.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_node = curr

        head = self.reverseList(head)
        return head
        
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev