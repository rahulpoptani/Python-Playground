'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''

from Common.Tags import LINKED_LIST, TWO_POINTER
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    if not head:
        return True

    slow = fast = head

    # Find the middle of the linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    left, right = head, prev

    # Compare the first half and the reversed second half
    while right:
        if left.val != right.val:
            return False

        left = left.next
        right = right.next

    return True

# Test cases
if __name__ == "__main__":
    # Example 1
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(isPalindrome(head1))  # Output: True

    # Example 2
    head2 = ListNode(1, ListNode(2))
    print(isPalindrome(head2))  # Output: False