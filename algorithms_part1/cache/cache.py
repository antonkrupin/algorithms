class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        sum = 0
        for i in range(len(key)):
            sum += 1
        return sum % self.size

    def is_key(self, key):
        for i in range(len(self.values)):
            if self.values[i] == key:
                return True
        return False

    def put(self, key, value):
        if not None in self.slots:
            minHitIndex = self.hits.index(min(self.hits))
            self.values[minHitIndex] = key
            self.slots[minHitIndex] = value
        else:
            index = self.hash_fun(key)
            self.values[index] = key
            self.slots[index] = value

    def get(self, key):
        if self.is_key(key):
            index = self.hash_fun(key)
            self.hits[index] = self.hits[index] + 1
            return self.slots[self.hash_fun(key)]
        else:
            return None
