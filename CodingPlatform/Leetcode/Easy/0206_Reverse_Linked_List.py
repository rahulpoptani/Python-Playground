'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''
from Common.Tags import LINKED_LIST
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev to the current node
        current = next_node       # Move to the next node

    return prev  # At the end, prev will be the new head of the reversed list

# test cases
def printList(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original list:")
printList(head1)
reversed_head1 = reverseList(head1)
print("Reversed list:")
printList(reversed_head1)   

# Example 2
head2 = ListNode(1, ListNode(2))
print("Original list:")
printList(head2)
reversed_head2 = reverseList(head2)
print("Reversed list:")
printList(reversed_head2)   

# Example 3
head3 = None
print("Original list:")
printList(head3)
reversed_head3 = reverseList(head3)
print("Reversed list:")
printList(reversed_head3)