class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    #asc = True храним по возрастанию 1, 2, 3
    #asc = False храним по убыванию 3, 2, 1
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
        pass
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

        # автоматическая вставка value 
        # в нужную позицию

    def find(self, val):
        return None # здесь будет ваш код

    def delete(self, val):
        pass # здесь будет ваш код

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        return 0 # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

#это не удаляем
"""
class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0
"""

ord = OrderedList(True)

ord.add(5)
ord.add(4)
ord.add(0)
ord.add(3)
ord.add(145)
ord.add(2)
ord.add(11)
ord.add(-1)

print('head', ord.head.value)
print('head prev', ord.head.prev)
print('head next', ord.head.next.value)
print('tail', ord.tail.value)
print('tail prev', ord.tail.prev.value)
print('tail next', ord.tail.next)
print('__________')
ord.print_all_nodes()