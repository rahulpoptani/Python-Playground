from Node import Node
from LinkedList import LinkedList

llist = LinkedList()
 
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second; # Link first node with second
second.next = third; # Link second node with the third node

llist.printList()

# insert data at head
llist.push(0)

llist.printList()

llist.insertAfter(llist.head.next.next, 5)

llist.printList()

llist.append(6)

llist.printList()

llist.printMiddle()

llist.deleteNodeByKey(3)

llist.printList()

llist.printMiddle()

llist.push(2)

print('Current Length of Linked List: {}'.format(llist.getLength()))

print('Searching for key: {}: {}'.format(2, llist.search(2)))

llist.deleteNodeByPosition(2)

llist.printList()

print('Searching for occurence of element: {} | Found at {} places'.format(2, llist.count(2)))

# llist.deleteLinkedList()

print('Detect Loop: {}'.format(llist.detectLoop()))

# llist.createLoop(2) # comment this otherwise looping will run indefinitely

print('Detect Loop: {}'.format(llist.detectLoop()))

print('Length of Loop: {}'.format(llist.lengthOfLoop()))

# Creating palindrome list
llist_palind = LinkedList()
llist_palind.head = Node(1)
llist_palind.append(2)
llist_palind.append(3)
llist_palind.append(2)
llist_palind.append(1)

print('Is the list Palindrome? {}'.format(llist_palind.isPalindrome()))

# linked list with duplicates
ll_dup = LinkedList()
ll_dup.append(1)
ll_dup.append(2)
ll_dup.append(2)
ll_dup.append(1)

ll_dup.printList()
ll_dup.removeConsecutiveDuplicates()
ll_dup.append(2)
ll_dup.append(3)
ll_dup.printList()
ll_dup.removeDuplicates()
ll_dup.printList()
ll_dup.append(4)
ll_dup.append(5)
ll_dup.printList()
# swap nodes
ll_dup.swapNodes(2,4)
ll_dup.printList()

ll_dup.moveLastToFront()
ll_dup.printList()