import ctypes
from random import randint

class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1
    
    def insert(self, index, itm):
        if index >= 0 and index <= self.count:
            if self.count + 1 > self.capacity:
                self.resize(self.capacity * 2)
            i = self.count
            while (i > index):
                self.array[i] = self.array[i - 1]
                i = i - 1
            self.array[index] = itm
            self.count = self.count + 1
        else:
            raise IndexError('Index is out of bounds')
    

da = DynArray()

testLen = randint(5,10)

for i in range(testLen):
    elem = randint(1,9)
    da.append(elem)
    print(da[i])

da.insert(4,50)
print('___________')

for elem in da:
    print(elem)








    



