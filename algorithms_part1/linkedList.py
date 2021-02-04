class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        headNode = self.head
        nodesList = []
        while headNode is not None:
            if headNode.value == val:
                nodesList.append(headNode)
            headNode = headNode.next
        if nodesList != []:
            return nodesList
        else:
            return []

    def delete(self, val, all=False):
        headNode = self.head

        if all == False:
            if headNode is not None:
                if headNode.value == val:
                    self.head = headNode.next
                    headNode = None
                    if self.head == None:
                        self.tail = None
                    return

            if headNode == None:
                self.tail = None
                return

            while headNode is not None:
                if headNode.value == val:
                    break
                prevNode = headNode
                headNode = headNode.next

            if headNode == None:
                return

            prevNode.next = headNode.next
            headNode = None
            self.tail = prevNode
        else:
            if self.head == None:
                return 

            while self.head is not None and self.head.value == val: 
                self.head = self.head.next
                if self.head == None:
                    self.tail = None

            if self.head is not None: 
                current = self.head
                while current.next is not None: 
                    if current.next.value == val: 
                        current.next = current.next.next 
                    else:
                        current = current.next
                self.tail = current

    def clean(self):
        self.__init__()
        
    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        startNode = self.head
        
        if self.head == None:
            self.head = Node(newNode)
            self.tail = self.head
            return

        if afterNode == None:
            self.head = Node(newNode)
            self.head.next = startNode
            return 

        while startNode is not None:
            if startNode.value == afterNode:
                nodeForAppend = Node(newNode)
                nextNodeLink = startNode.next
                nodeForAppend.next = nextNodeLink
                startNode.next = nodeForAppend
                if startNode.next.next == None:
                    self.tail = nodeForAppend
            startNode = startNode.next
            
