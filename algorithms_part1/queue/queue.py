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
    
    def rotateQueue(self, value):
        if value == 0 or len(self.queue) == 0:
            return self.queue
        
        if value > len(self.queue):
            rotateCf = value % len(self.queue)
            for i in range(rotateCf):
                el = self.queue[0]
                newQueue = self.queue[1:] + [el]
                self.queue = newQueue
            return self.queue
        else:
            rotateCf = value
            for i in range(rotateCf):
                el = self.queue[0]
                newQueue = self.queue[1:] + [el]
                self.queue = newQueue
            return self.queue
