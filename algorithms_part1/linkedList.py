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
            if self.head == None:
                return 

            while self.head is not None and self.head.value == val: 
                self.head = self.head.next

            if self.head is not None: 
                current = self.head
                while current.next is not None: 
                    if current.next.value == val: 
                        current.next = current.next.next 
                    else:
                        current = current.next

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

#test = [2,2,2,2,2,2,2,2,2,2,2,2,11,1,51,6,1,5,1,1,2,2,2,2,2,2,1,1,1,1,2,2,2,2]
#test = [2,2,2,2,2,2,2,2,2,2,2,2,2]
test = [2,5,2,24,3,2,2,6]
#test = [2,2,5,2,4]
#test = [1,1,1,1,2,2,2,2,2,2,2,2,2,1]
#test = [5,4,5,5,5,5,5,5,5,5,5,5,5]
s_list = LinkedList()

for i in test:
    s_list.add_in_tail(Node(i))
s_list.print_all_nodes()
print('_____')
s_list.delete(6)
s_list.print_all_nodes()
