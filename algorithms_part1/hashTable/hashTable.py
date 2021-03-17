class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        sum = 0
        for i in range(len(value)):
            sum += 1
        return sum % self.size

    def seek_slot(self, value):
        if self.slots[self.hash_fun(value)] != None:
            start = self.hash_fun(value)
            for i in range(self.size):
                if i == start:
                    continue
                else:
                    if self.slots[i] == None:
                        return i
        else:
            return self.hash_fun(value)
        return None

    def put(self, value):
        index = self.seek_slot(value)
        if index == None:
            return None
        else:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        for i in range(self.size):
            if self.slots[i] == value:
                return i
        return None
