test = [2,13,2,4,35,13,99,18,13,123,2,1,10,15,6]

class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

n1 = Node(12)
n2 = Node(55)
n1.next = n2

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
                    #headNode = None
                    prevNode = headNode
                    headNode = headNode.next
                    #return
            
            while headNode is not None:
                if headNode.value == val:
                    prevNode.next = headNode.next
                prevNode = headNode
                headNode = headNode.next

            if headNode == None:
                return

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

#[2,13,2,4,35,13,99,18,13,123,2,1,10,15,6]
s_list = LinkedList()

for i in test:
    s_list.add_in_tail(Node(i))

s_list.print_all_nodes()
print('____')
s_list.delete(6, all=True)
s_list.print_all_nodes()
#s_list.delete(13, all=True)
#print('______')
#print(s_list.len())
#print('_____')
#s_list.print_all_nodes()
