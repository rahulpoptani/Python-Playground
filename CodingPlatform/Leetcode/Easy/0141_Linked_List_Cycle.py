'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''
from Common.Tags import GRIND_75, LINKED_LIST, TWO_POINTER, HASHMAP

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

def hasCycle2(head: Optional[ListNode]) -> bool:
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False

# Test cases
if __name__ == "__main__":
    # Example 1
    head1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle
    print(hasCycle(head1))  # Output: True
    print(hasCycle2(head1))  # Output: True

    # Example 2
    head2 = ListNode(1)
    node5 = ListNode(2)
    head2.next = node5
    node5.next = head2  # Creates a cycle
    print(hasCycle(head2))  # Output: True
    print(hasCycle2(head2))  # Output: True

    # Example 3
    head3 = ListNode(1)
    print(hasCycle(head3))  # Output: False
    print(hasCycle2(head3))  # Output: False