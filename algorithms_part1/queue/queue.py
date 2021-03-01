class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        appendEl = [item]
        self.queue = self.queue + appendEl

    def dequeue(self):
        if len(self.queue) > 0:
            firstEl = self.queue[0]
            self.queue = self.queue[1:]
            return firstEl
        else:
            return None 

    def size(self):
        return len(self.queue)
