class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        appendEl = [item]
        self.deque = appendEl + self.deque

    def addTail(self, item):
        appendEl = [item]
        self.deque = self.deque + appendEl

    def removeFront(self):
        if len(self.deque) > 0:
            firstEl = self.deque[0]
            self.deque = self.deque[1:]
            return firstEl
        else:
            return None

    def removeTail(self):
        if len(self.deque) > 0:
            lastEl = self.deque[-1]
            self.deque = self.deque[:-1]
            return lastEl
        else:
            return None

    def size(self):
        return len(self.deque)

