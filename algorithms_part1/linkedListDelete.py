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

    def delete(self, val, all=False):
        if self.head is None:
            return
        
        if self.head.value == val:
            self.head = self.head.next
            
        prevNode = self.head
        n = self.head

        while n is not None:
            if n.value == val:
                n = n.next
                continue
            print(n.value)
            prevNode = n
            n = n.next

            
            #headNode = headNode.next

        """
        n = self.head
        while n.next is not None:
            if n.next.value == val:
                self.head = self.head.next
            n = n.next
        """
        
            

#test = [2,11,1,51,6,1,5,1,1,1,1,1,1]
test = [2,2,5,2,2,4,3,2,2,6]

s_list = LinkedList()

for i in test:
    s_list.add_in_tail(Node(i))

print('_______')
print(s_list.delete(2, all=True))
s_list.print_all_nodes()
