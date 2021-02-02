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
        
        currentNode = self.head
        
        if currentNode is None:
            return
        
        if currentNode is not None:
            if currentNode.value == val:
                self.head = self.head.next
                currentNode = self.head

        previousNode = currentNode

        while currentNode is not None:
            if currentNode.value == val:
                previousNode.next = currentNode.next
                currentNode = currentNode.next
                continue
            previousNode = currentNode
            currentNode = currentNode.next
        
test = [2,2,2,2,2,2,2,2,2,2,2,2,11,1,51,6,1,5,1,1,2,2,2,2,2,2,1,1,1,1,2,2,2,2]
#test = [2,2,2,2,2,2,2,2,2,2,2,2,2]
#test = [2,2,5,2,2,4,3,2,2,6]
#test = [1,1,1,1,2,2,2,2,2,2,2,2,2,1]
#test = [5,4,5,5,5,5,5,5,5,5,5,5,5]
s_list = LinkedList()

for i in test:
    s_list.add_in_tail(Node(i))
s_list.print_all_nodes()
print('_____')
s_list.delete(2)
s_list.print_all_nodes()
