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
    
    def delete(self, val, all=False):
        node = self.head
        if all == False:
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
                newNode.prev = None
                newNode.next = None
            else:
                oldTail = self.tail
                self.tail = newNode
                oldTail.next = newNode
                newNode.prev = oldTail
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode.value:
                    if node.next == None:
                        oldTail = self.tail
                        self.tail = newNode
                        oldTail.next = newNode
                        newNode.prev = oldTail
                        break
                    else:
                        newNode.next = node.next
                        node.next = newNode
                        newNode.prev = node
                        node.next.next.prev = newNode
                        #node.next.prev = newNode
                        break
                node = node.next
    
    def add_in_head(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
            self.tail = item
        elif self.head.next is None:
            headElem = self.head
            self.head = item
            self.tail = headElem
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            headElem = self.head
            self.head = item
            self.head.prev = None
            self.head.next = headElem
            self.head.next.prev = self.head
            
"""
s_list = LinkedList2()
s_list.add_in_head(Node(22))
print('len', s_list.len())
s_list.delete(22)
"""
"""
s_list.add_in_head(Node(16))
s_list.insert(Node(16), Node(88))
s_list.add_in_head(Node(19))
s_list.insert(Node(88), Node(1))
s_list.delete(16)
s_list.add_in_tail(Node(15))
s_list.add_in_head(Node(15))
s_list.insert(Node(88),Node(15))
s_list.delete(15, all=True)
"""
"""
print('head', s_list.head)
print('tail', s_list.tail)
#print('head',s_list.head.value)
#print('head prev', s_list.head.prev)
#print('head next', s_list.head.next.value)
#print('tail', s_list.tail.value)
#print('tail prev', s_list.tail.prev.value)
#print('tail prev prev', s_list.tail.prev.prev.value)
#print('tail next', s_list.tail.next)
print('______________')
s_list.print_all_nodes()
print('_____________')
print('len', s_list.len())
"""
#разобраться с Head and prev next

