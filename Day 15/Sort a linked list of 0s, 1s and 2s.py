"""Given a linked list of 0s, 1s and 2s, The task is to sort and print it.
Examples: 
Input: 1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL 
Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL

Input: 1 -> 1 -> 2 -> 1 -> 0 -> NULL 
Output: 0 -> 1 -> 1 -> 1 -> 2 -> NULL """


# Python Program to sort a linked list of 0s, 1s or 2s

# A linked list node
class Node:
  
      # Constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to sort a linked list of 0s, 1s and 2s
def sort_list(head):
  
    # Initialize count of '0', '1' and '2' as 0
    cnt = [0, 0, 0]
    ptr = head

    # Traverse and count total number of '0', '1' and '2'
    # cnt[0] will store total number of '0's
    # cnt[1] will store total number of '1's
    # cnt[2] will store total number of '2's
    while ptr is not None:
        cnt[ptr.data] += 1
        ptr = ptr.next

    idx = 0
    ptr = head
    
    # Fill first cnt[0] nodes with value 0
    # Fill next cnt[1] nodes with value 1
    # Fill remaining cnt[2] nodes with value 2
    while ptr is not None:
        if cnt[idx] == 0:
            idx += 1
        else:
            ptr.data = idx
            cnt[idx] -= 1
            ptr = ptr.next

# This function prints the contents 
# of the linked list starting from the head
def print_list(node):
    while node is not None:
        print(f" {node.data}", end='')
        node = node.next
    print("\n")

# Driver code
if __name__ == "__main__":
  
    # Create a hard-coded linked list:
    # 1 -> 1 -> 2 -> 1 -> 0 -> NULL
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)

    print("Linked List before Sorting:", end='')
    print_list(head)

    # Function to sort the linked list
    sort_list(head)

    print("Linked List after Sorting:", end='')
    print_list(head)