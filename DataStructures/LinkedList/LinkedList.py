from Node import Node

class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        temp = self.head
        out = ""
        out += str(temp.data)
        while temp.next:
            out += (" " + str(temp.next.data))
            temp = temp.next
        return out
    
    # Time: O(1)
    def getHead(self):
        return self.head
    
    # Time: O(1)
    @property
    def is_empty(self):
        if self.head is None: 
            return True
        else: 
            return False
     
    # This function prints contents of linked list starting from head
    def printList(self):
        if not self.is_empty:
            temp = self.head
            while temp:
                print(temp.data, end=' ')
                temp = temp.next
            print()
    
    # Length on Linked List: O(n)
    @property
    def getLength(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count
    
    # Insert at head: O(1)
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Insert node at the end: O(n)
    def append(self, new_data):
        new_node = Node(new_data)
        if self.is_empty:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    # Insert node at specific index: O(n)
    def insert(self, index, new_data):
        new_node = Node(new_data)
        if self.is_empty:
            self.head = new_node
        else:
            if index == 0:
                self.push(new_data)
            elif index >= self.getLength-1: # Either at tail or above total length
                self.append(new_data)
            else:
                tmp = self.head
                counter = 1
                while counter < index:
                    counter += 1
                    tmp = tmp.next
                next_to_tmp = tmp.next
                tmp.next = new_node
                new_node.next = next_to_tmp
    
    # Search element in Linked List: O(n)
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    # Delete at head: O(1)
    def delete_at_head(self):
        temp = self.head
        if temp:
            self.head = temp.next
            temp = None
            return True
    
    # Delete at tail: O(n)
    def delete_at_tail(self):
        if self.is_empty:
            return False
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return True
    
    # Delete element by key: O(n)
    def deleteByKey(self, key):
        if self.is_empty:
            return False
        temp = self.head
        prev = None
        # if key found at head
        if temp.data == key:
            self.delete_at_head()
            return True
        # otherwise traverse
        while temp:
            if temp.data == key:
                prev.next = temp.next
                temp = None
                return True
            prev = temp
            temp = temp.next
        return False
    
    def deleteNodeByPosition(self, position):
        # if linked list is empty
        if self.is_empty:
            return False
        temp = self.head
        # Delete at head position
        if position == 0:
            return self.delete_at_head()
        # Find previous node from position need to be deleted
        for _ in range(position-1):
            temp = temp.next
            if temp is None:
                return False        
        # unlink the node
        next = temp.next.next
        temp.next = None
        temp.next = next
        return True
    
    def deleteLinkedList(self):
        self.head = None
        return True
    
    # Reverse Linked List: O(n)
    # 3 pointer approach. Keep track of previous, current and next node in sequence.
    # Initially previous is null, change current pointer which is pointing to next to previous.
    # The link is broken and now current is pointing to previous.
    # Move ahead, make prev as current and current as next, and next as next next.
    def reverse(self):
        if self.is_empty:
            return False
        prev = None # Pointer 1 - maintain track of previous node
        current = self.head # Pointer 2 - the current node which is head initially
        # reversal
        while current:
            next = current.next # Pointer 3 - next node of current node
            current.next = prev
            prev = current
            current = next
            # set the last element as the new head node
            self.head = prev
        return True
    
    # Detect Loop in Linked List: O(n)
    def detectLoop(self):
        visited = set()
        temp = self.head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False
    
    # Create Loop by connecting last node to nth node: O(n)
    def createLoop(self, n):
        LoopNode = self.head
        if n > self.getLength:
            return False
        for _ in range(1, n):
            LoopNode = LoopNode.next
        # end is the last node of linked list
        end = self.head
        while end.next:
            end = end.next
        end.next = LoopNode
        return True
    
    # Find middle element in Linked List: O(n)
    def findMiddle(self):
        # initialize two pointers, slow (step 1 at a time) and fast (step 2 at a time)
        if self.is_empty:
            return None
        # If only 1 element
        if self.head.next is None:
            return self.head
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    def find_mid(self):
        if self.is_empty:
            return None
        # If only 1 element
        if self.head.next is None:
            return self.head
        node = self.head
        mid = 0
        len = self.getLength
        if len % 2 == 0:
            mid = len//2
        else:
            mid = len//2 + 1
        for _ in range(mid-1):
            node = node.next
        return node.data
    
    # Remove duplicates from Linked List: O(n)
    def removeDuplicates(self):
        if self.head is None or self.head.next is None:
            return
        hash = set()
        current = self.head
        hash.add(current.data)
        while current.next:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
    

    # Union of two linked list - Note: Union does not include repeated elements: O(m+n)
    def union(self, ll):
        if not self.is_empty and not ll.is_empty:
            hash = set()
            first = self.head
            second = ll.head
            while first:
                hash.add(first.data)
                first = first.next
            while second:
                if not second.data in hash:
                    self.append(second.data)
                second = second.next
    
    # Intersection of two linked list - Note: Intersection contains only common elements
    def intersection(self, ll):
        first = self.head
        second = ll.head
        map = {}
        # load all values from linked list 1 to map
        while first:
            map[first.data] = 1
            first = first.next
        # check whether linked list 2 values are available in map, if then increment by 1
        while second:
            if second.data in map:
                map[second.data] = map[second.data] + 1
            second = second.next
        # loop over map and identify keys with only 1 value.
        for key, value in map.items():
            if value == 1:
                self.deleteByKey(key)
    
    # Get value of nth node from head: O(n)
    def get_node_from_head(self, index):
        current = self.head
        count = 1
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return -1
    
    # Get value of nth node from tail: O(n)
    def get_node_from_tail(self, index):
        if self.is_empty or index > self.getLength:
            return -1
        return self.get_node_from_head(self.getLength - index + 1)
    
    # Length of loop
    def lengthOfLoop(self):
        if self.is_empty:
            return 0
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
        ispalin = False
        # push all elements into stack
        while temp:
            stack.append(temp.data)
            temp = temp.next
        # iterate again and compare with stack pop last element
        temp = self.head
        while temp:
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
    
    
    

