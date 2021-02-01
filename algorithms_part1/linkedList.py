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

    def delete(self, val, all=False):
        headNode = self.head

        if all == False:
            if headNode is not None:
                if headNode.value == val:
                    self.head = headNode.next
                    headNode = None
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
        else:
            if headNode is not None:
                if headNode.value == val:
                    self.head = headNode.next
                    prevNode = headNode
                    headNode = headNode.next
            
            while headNode is not None:
                if headNode.value == val:
                    prevNode.next = headNode.next
                prevNode = headNode
                headNode = headNode.next

            if headNode == None:
                return

    def clean(self):
        self.__init__()
        
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
            return None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        startNode = self.head
        
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
            startNode = startNode.next
