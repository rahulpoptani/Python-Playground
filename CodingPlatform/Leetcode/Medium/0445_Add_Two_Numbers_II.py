from Common.Tags import LINKED_LIST
from typing import Optional

'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
        current = self
        while current:
            print(current.val, end=" ")
            current = current.next
        print()        


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    s1 = []
    s2 = []

    while l1:
        s1.append(l1)
        l1 = l1.next
    while l2:
        s2.append(l2)
        l2 = l2.next

    carry = 0
    head = None

    while s1 or s2 or carry:
        total = carry
        if s1:
            total += s1.pop().val
        if s2:
            total += s2.pop().val

        carry = total // 10
        new_node = ListNode(total % 10)
        new_node.next = head
        head = new_node

    return head

addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), ListNode(5, ListNode(6, ListNode(4)))).print()
addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))).print()
addTwoNumbers(ListNode(0), ListNode(0)).print()