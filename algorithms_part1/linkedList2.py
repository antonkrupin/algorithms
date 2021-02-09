class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            headElem = self.head
            self.head = item
            self.head.prev = None
            self.head.next = headElem
            
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
        node = self.head
        nodesList = []
        while node is not None:
            if node.value == val:
                nodesList.append(node)
            node = node.next

        return nodesList

    def len(self):
        length = 0
        while self.head is not None:
            length += 1
            self.head = self.head.next
        return length
    
    def delete(self, val, all=False):
        node = self.head
        if all == False:
            while node is not None:
                if node.value == val:
                    if node.prev == None:
                        if self.head.next == None:
                            self.head == None
                            self.tail == None
                        else:
                            self.head.next.prev = None
                            self.head = self.head.next
                    else:
                        if node.next == None:
                            node.prev.next = None
                            self.tail = node.prev
                        else:
                            node.prev.next = node.next
                            node.next.prev = node.prev
                    return True
                else:
                    node = node.next
            return False
        else:
            while node is not None:
                if node.value == val:
                    if node.prev == None:
                        if self.head.next == None:
                            self.head = None
                            self.tail = None
                        else:
                            self.head.next.prev = None
                            self.head = self.head.next
                    else:
                        if node.next == None:
                            node.prev.next = None
                            self.tail = node.prev
                        else:
                            node.prev.next = node.next
                            node.next.prev = node.prev
                node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def insert(self, afterNode, newNode):
        if afterNode == None:
            if self.head == None:
                self.head = newNode
                self.tail = newNode
                newNode.next = None
                newNode.prev = None
            else:
                self.tail.next = newNode
                self.tail.prev = self.tail
                self.tail = newNode
        else:
            node = self.head
            if node.value == afterNode.value:
                if node.next == None:
                    node.next = newNode
                    newNode.prev = node
                    newNode.next = None
                    self.tail = newNode
                else:
                    newNode.next = node.next
                    newNode.prev = node
                    node.next = newNode
                    node.next.prev = newNode
                node = node.next

    
