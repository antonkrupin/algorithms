class PowerSet:
    def __init__(self):
        self.powerset = []

    def size(self):
        length = 0
        for i in range(len(self.powerset)):
            length += 1
        return length
        
    def put(self, value):
        for i in self.powerset:
            if i == value:
                return -1
        appendElem = [value]
        self.powerset = self.powerset + appendElem
        
    def get(self, value):
        try:
            self.powerset.index(value)
            return True
        except ValueError:
            return False

    def remove(self, value):
        for i in range(len(self.powerset)):
            if self.powerset[i] == value:
                startSet = self.powerset[:i]
                endSet = self.powerset[i+1:]
                self.powerset = startSet + endSet
                return True
        return False

    def intersection(self, set2):
        intersectionSet = PowerSet()
        for i in self.powerset:
            if set2.get(i):
                intersectionSet.put(i)
        
        return intersectionSet.powerset

    def union(self, set2):
        unionSet = self.intersection(set2)
        
        for i in self.powerset:
            if (i in unionSet) == False:
                unionSet.append(i)
        
        for i in set2.powerset:
            if (i in unionSet) == False:
                unionSet.append(i)

        return unionSet

    def difference(self, set2):
        differenceSet = PowerSet()
        for i in self.powerset:
            if set2.get(i) == False:
                differenceSet.put(i)

        return differenceSet.powerset

    def issubset(self, set2):
        counter = 0
        for i in self.powerset:
            if set2.get(i):
                counter += 1
        
        if counter == set2.size():
            return True
        else:
            return False
