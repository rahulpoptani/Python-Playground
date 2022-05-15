from Node import Node
from LinkedList import LinkedList

# Initialize Linked List
ll1 = LinkedList()
 
# Populate the linked list manually
first = Node(1)
second = Node(2)
third = Node(3)
ll1.head = first  # Add first element as head
first.next = second # Link first node with second
second.next = third # Link second node with the third node
print('Print linked list')
ll1.printList()


# Insert data at head
print('Insert 0 at head')
ll1.push(0)
ll1.printList()


# Insert data at tail
print('Insert 4 at tail')
ll1.append(4)
ll1.printList()


# Insert element at Index
ll2 = LinkedList()
print('Inserted 9 at Index 0')
ll2.insert(0, 9)
ll2.printList()
print('Inserted 8 at Index 0')
ll2.insert(0, 8)
ll2.printList()
print('Inserted 7 at Index 5 - Index Does not exists, hence will insert at tail')
ll2.insert(5, 7)
ll2.printList()
print('Inserted 6 at Index 1')
ll2.insert(1, 6)
ll2.printList()
print('Inserted 5 at Index 1')
ll2.insert(1, 5)
ll2.printList()
print('Inserted 4 at Index 0')
ll2.insert(0, 4)
ll2.printList()
print('Inserted 3 at Index 2')
ll2.insert(2, 3)
ll2.printList()
print('Inserted 2 at Index 11')
ll2.insert(11, 2)
ll2.printList()


# Search a element in Linked List
print(f'Searching element 1 in Linked List: {ll2.search(1)}')
print(f'Searching element 4 in Linked List: {ll2.search(4)}')


# Delete a element from Linked List
print(f'Deleted element 5 from Linked List: {ll2.deleteByKey(5)}')
ll2.printList()
print(f'Deleted element 4 from Linked List: {ll2.deleteByKey(4)}')
ll2.printList()
print(f'Deleted element 2 from Linked List: {ll2.deleteByKey(2)}')
ll2.printList()
print(f'Deleted element 2 from Linked List: {ll2.deleteByKey(2)}')
ll2.printList()
print(f'Deleted current head from Linked List: {ll2.delete_at_head()}')
ll2.printList()


# Delete Node by position
print('---------------------------------------------------------------------')
print(f'Deleted Index 0 from Linked List: {ll2.deleteNodeByPosition(0)}')
ll2.printList()
print(f'Deleted Index 1 from Linked List: {ll2.deleteNodeByPosition(1)}')
ll2.printList()
print(f'Delete at tail: {ll2.delete_at_tail()}')
ll2.printList()
print(f'Delete Linked List: {ll2.deleteLinkedList()}')
ll2.printList()


# Create new Linked List and additing 0,1,2,3,4,5
print('---------------------------------------------------------------------')
ll3 = LinkedList()
for x in range(6):
    ll3.append(x)
print(f'Created new Linked List 0,1,2,3,4,5')
ll3.printList()
print(f'Reverse Linked List: {ll3.reverse()}')
ll3.printList()


# Add Loop and Detect Loop
print(f'Detect Loop in Linked List: {ll3.detectLoop()}')
print(f'Create Loop at Index 2: {ll3.createLoop(2)}')
print(f'Detect Loop in Linked List: {ll3.detectLoop()}')
print(f'Length of Loop: {ll3.lengthOfLoop()}')


# Create new Linked List and additing 0,1,2,3,4
print('---------------------------------------------------------------------')
ll4 = LinkedList()
for x in range(0,5):
    ll4.append(x)
print(f'Created new Linked List 0,1,2,3,4')
ll4.printList()
print(f'Find Middle Element in Linked List: {ll4.findMiddle()}')
print(f'Find Middle Element in Linked List: {ll4.find_mid()}')
print(f'Insert duplicate element 0,1 in Linked List')
ll4.append(0)
ll4.append(1)
ll4.printList()
print(f'Insert 5,6 in Linked List')
ll4.append(5)
ll4.append(6)
ll4.printList()
print(f'Removing duplicate elements from Linked List')
ll4.removeDuplicates()
ll4.printList()


# Union of two Linked List
print('---------------------------------------------------------------------')
print('Create List 1 with 1,2,3,4,5')
ll5 = LinkedList()
for _ in range(1,6):
    ll5.append(_)
ll5.printList()
print('Create List 2 with 4,5,6,7')
ll6 = LinkedList()
for _ in range(4,8):
    ll6.append(_)
ll6.printList()
print(f'Union of List 1 and List 2')
ll5.union(ll6)
ll5.printList()
print('Removing values 6,7 List 1')
ll5.deleteByKey(6)
ll5.deleteByKey(7)
ll5.printList()
print(f'Intersection of List {ll5} and List {ll6}')
ll5.intersection(ll6)
ll5.printList()


# Find Nth Node from Head and Tail
print('---------------------------------------------------------------------')
print('Create List with 1,2,3,4,5')
ll7 = LinkedList()
for _ in range(1,6):
    ll7.append(_)
ll7.printList()
print(f'Get 2nd node from Head {ll7.get_node_from_head(2)}')
print(f'Get 2nd node from Tail {ll7.get_node_from_tail(2)}')
print(f'Is the list Palindrome? {ll7.isPalindrome()}')


# Creating palindrome list
print('---------------------------------------------------------------------')
llist_palind = LinkedList()
llist_palind.append(1)
llist_palind.append(2)
llist_palind.append(3)
llist_palind.append(2)
llist_palind.append(1)
llist_palind.printList()

print('Is the list Palindrome? {}'.format(llist_palind.isPalindrome()))

# # linked list with duplicates
# ll_dup = LinkedList()
# ll_dup.append(1)
# ll_dup.append(2)
# ll_dup.append(2)
# ll_dup.append(1)

# ll_dup.printList()
# ll_dup.removeConsecutiveDuplicates()
# ll_dup.append(2)
# ll_dup.append(3)
# ll_dup.printList()
# ll_dup.removeDuplicates()
# ll_dup.printList()
# ll_dup.append(4)
# ll_dup.append(5)
# ll_dup.printList()
# # swap nodes
# ll_dup.swapNodes(2,4)
# ll_dup.printList()

# ll_dup.moveLastToFront()
# ll_dup.printList()

# ll_dup.reverse()
# ll_dup.printList()

# newll = ll_dup.splitEvenOdd()
# newll.printList()