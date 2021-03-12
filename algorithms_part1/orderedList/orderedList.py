class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0

    def add(self, value):
        item = Node(value)
        if self.head is None:
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
        else:
            node = self.head
            while node is not None:
                if ((self.__ascending == True and 
                    (self.compare(item.value, node.value) == -1 or self.compare(item.value, node.value) == 0)) or
                    (self.__ascending == False and 
                    (self.compare(item.value, node.value) == 1 or self.compare(item.value, node.value) == 0 ))):
                    if node.prev == None:
                        self.head.prev = item
                        item.next = self.head
                        self.head = item
                        item.prev = None
                        break
                    else:
                        node.prev.next = item
                        item.prev = node.prev
                        item.next = node
                        node.prev = item
                        break
                else:
                    if node.next == None:
                        node.next = item
                        item.prev = node
                        item.next = None
                        self.tail = item
                        break

                node = node.next

    def find(self, val):
        nodeValue = val
        if ((self.__ascending == True and (self.compare(nodeValue, self.head.value) == -1 or self.compare(nodeValue, self.tail.value) == 1)) or
            (self.__ascending == False and (self.compare(nodeValue, self.head.value) == 1 or self.compare(nodeValue, self.tail.value) == -1))):
            return None
        else:
            node = self.head
            while node is not None:
                if self.compare(nodeValue, node.value) == 0:
                    return node
                node = node.next
            return None

    def delete(self, val):
        node = self.head
        if node == None:
            return False
        if (node.prev == None and node.next == None) and node.value == val:
            self.head = None
            self.tail = None
            return True
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
            
    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        counter = 0
        while node is not None:
            counter += 1
            node = node.next
        return counter

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r
    

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        string1 = str(v1).strip()
        string2 = str(v2).strip()

        if string1 > string2:
            return 1
        elif string1 < string2:
            return -1
        else:
            return 0
