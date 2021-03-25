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
        for i in self.powerset:
            if i == value:
                return True
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
        intersectionSet = set()
        for i in self.powerset:
            for j in set2:
                if j == i:
                    intersectionSet.add(i)
        
        if len(intersectionSet) != 0:
            return intersectionSet
        else:
            return None

    def union(self, set2):
        unionSet = self.powerset
        for i in set2:
            if self.get(i) == False:
                unionSet = unionSet + [i]

        if len(unionSet) != 0:
            return set(unionSet)
        else:
            return None

    def difference(self, set2):
        differenceSet = set()
        for i in self.powerset:
            counter = 0
            for j in set2:
                if j != i:
                    counter += 1              
            if counter == len(set2):
                differenceSet.add(i)

        if len(differenceSet) != 0:
            return differenceSet
        else:
            return None

    def issubset(self, set2):
        counter = 0
        for i in set2:
            if self.get(i):
                counter += 1
        if counter == len(set2):
            return True
        else:
            return False
