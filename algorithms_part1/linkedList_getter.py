class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    """
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, item):
        self.__age = item
    """

    def getHead(self):
        return self.__head

    def setHead(self, value):
        self.__head = value

    def getTail(self):
        return self.__tail

    def setTail(self, value):
        self.__tail = value

    def add_in_tail(self, item):
        if self.getHead() is None:
            #self.head = item
            self.setHead(item)
        else:
            #self.tail.next = item
            test = self.getTail()
            self.setTail(test).next
            #self.setTail(item) = item
        #self.tail = item
        self.setTail(item)

    def print_all_nodes(self):
        node = self.getHead()
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
        if afterNode == None:
            if self.head == None:
                self.head = newNode
                self.tail = newNode
                newNode.next = None
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            node = self.head
            while node != None:
                if node.value == afterNode.value:
                    if node.next == None:
                        node.next = newNode
                        self.tail = newNode
                        newNode.next = None
                    else:
                        newNode.next = node.next
                        node.next = newNode
                node = node.next

s_list = LinkedList()

s_list.add_in_tail(Node(5))
s_list.add_in_tail(Node(5))
s_list.print_all_nodes()

