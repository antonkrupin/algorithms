import random
class ListWithConstructor:
    def __init__(self, start):
        self.start = start
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1

        if self.count < 10:
            return current

        raise StopIteration


class ListWithConstructorInfinite:
    def __init__(self, iterateElemQuantity, infinityFlag):
        self.iterateElemQuantity = iterateElemQuantity
        self.infinityFlag = infinityFlag

    def __iter__(self):
        self.start = 1
        self.count = 0
        return self

    def __next__(self):
        current = self.start 
        self.start = self.start + 1
        self.count += 1

        if self.infinityFlag == True:
            if self.count < self.iterateElemQuantity:
                return current
            else:
                self.count = 0
                self.start = 1
                return current
        else:
            if self.count <= self.iterateElemQuantity:
                return current
        
        raise StopIteration
