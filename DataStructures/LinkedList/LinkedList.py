from Node import Node

class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
     
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    # insert at head of node
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # add node at specific position
    def insertAfter(self, prev_node, new_data):
        # check if prev_node exists
        if prev_node is None:
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    # add node at the end: O(n)
    def append(self, new_data):
        new_node = Node(new_data)
        # if linked list is empty, make new node as head
        if self.head is None:
            self.head = new_node
            return
        
        # else traverse till the end node
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
    
    # delete a node
    def deleteNodeByKey(self, key):
        # store head node
        temp = self.head

        # if head node itself holds the key to be delete
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        
        # search for the key to be deleted, keep track of previous node as need to change prev.next
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        # if key is not present in linked list
        if (temp == None):
            return
        
        prev.next = temp.next
        temp = None
    
    def deleteNodeByPosition(self, position):
        # if linked list is empty
        if self.head == None:
            return
        
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        # Find previous node from position need to be deleted
        for x in range(position-1):
            temp = temp.next
            if temp is None:
                break
        
        # if the position is more than number of nodes
        if temp is None:
            return
        
        if temp.next is None:
            return
        
        next = temp.next.next

        # unlink the node
        temp.next = None
        temp.next = next
    
    def deleteLinkedList(self):
        self.head = None
    
    def getLength(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count
    
    def search(self, key):
        current = self.head
        
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        
        return False
    
    def getNthNode(self, index):
        current = self.head
        count = 0
        while(current):
            if count == index:
                return current.data
            count += 1
            current = current.next
        
        return 0
    
    def printMiddle(self):
        # initialize two pointers, slow (step 1 at a time) and fast (step 2 at a time)
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print('The middle element is: {}'.format(slow.data))
    
    def count(self, search_for):
        current = self.head
        count = 0
        while(current is not None):
            if current.data == search_for:
                count += 1
            current = current.next
        return count
    
    def detectLoop(self):
        visited = set()
        temp = self.head
        while(temp):
            if (temp in visited):
                return True
            visited.add(temp)
            temp = temp.next
        return False
    
    # connect last node to nth node
    def createLoop(self, n):
        LoopNode = self.head
        for _ in range(1, n):
            LoopNode = LoopNode.next
        
        # end is the last node of linked list
        end = self.head
        while(end.next):
            end = end.next
        
        end.next = LoopNode
    
    def lengthOfLoop(self):
        if self.head is None: return 0
        
        loopExists = self.detectLoop()

        if loopExists:
            slow = self.head
            fast = self.head
            flag = 0

            while (slow and slow.next and fast and fast.next and fast.next.next):
                if slow == fast and flag != 0:
                    count = 1
                    slow = slow.next
                    while(slow != fast):
                        slow = slow.next
                        count += 1
                    return count
                
                slow = slow.next
                fast = fast.next.next
                flag = 1
    
    def isPalindrome(self):
        temp = self.head
        stack = []
        ispalin = True

        # push all elements into stack
        while(temp):
            stack.append(temp.data)
            temp = temp.next
        
        # iterate again and compare with stack pop last element
        temp = self.head
        while(temp):
            stackElement = stack.pop()
            if temp.data == stackElement:
                ispalin = True
            else:
                ispalin = False
                break
            
            temp = temp.next
        
        return ispalin
    
    # remove consecutive duplicates
    def removeConsecutiveDuplicates(self):
        temp = self.head
        if temp is None:
            return
        
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
    
    def removeDuplicates(self):
        if self.head is None or self.head.next is None:
            return
        
        hash = set()
        current = self.head
        hash.add(current.data)

        while(current.next):
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
    
    def swapNodes(self, x, y):
        # nothing to do if x and y are same
        if x == y: return

        prevX = None
        currX = self.head
        # search for X, keep track of previous and current X
        while currX is not None and currX.data != x:
            prevX = currX
            currX = currX.next
        
        prevY = None
        currY = self.head
        while currY is not None and currY.data != y:
            prevY = currY
            currY = currY.next
        
        if currX == None or currY == None:
            return
        
        if prevX is not None:
            prevX.next = currY
        else: # when this will be true?
            self.head = currY
        
        if prevY is not None:
            prevY.next = currX
        else:
            self.head = currX
        
        # swap pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
    
    def moveLastToFront(self):
        temp = self.head
        prevNode = None
        
        if not temp or not temp.next: return

        while temp and temp.next:
            prevNode = temp
            temp = temp.next
        
        # point second last to None
        prevNode.next = None
        # make last node as first node
        temp.next = self.head
        self.head = temp
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    

