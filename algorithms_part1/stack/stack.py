class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) > 0:
            value = self.stack[-1]
            self.stack = self.stack[:-1]
            return value
        else:
            return None

    def push(self, value):
        tempEl = [value]
        self.stack = self.stack + tempEl
    
    def peek(self):
        if len(self.stack) > 0:
            value = self.stack[-1]
            return value
        else:
            return None 

stack = Stack()

stack = Stack()
stack.push(1)
stack.push("2")
stack.push(3.14)
while stack.size() > 0:
    print(stack.pop())