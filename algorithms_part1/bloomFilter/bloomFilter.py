class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        #self.bitArray = self.set_bit(0b00000000000000000000000000000000, self.filter_len)
        self.bitArray = 0b00000000000000000000000000000000 | (1 << self.filter_len)

    def set_bit(self, A,k):
        return A | (1 << k)

    def hash1(self, str1):
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 17 + code) % 32
        return res
        
    def hash2(self, str1):
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 223 + code) % 32
        return res

    def add(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        self.bitArray = self.bitArray | h1
        self.bitArray = self.bitArray | h2

    def is_value(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        #temp = 0b00000000000000000000000000000000 | (1 << self.filter_len)
        temp = self.bitArray
        test = temp | h1
        #print('temp | h1', bin(temp | h1))
        test1 = test | h2
        #print('temp | h2', bin(temp | h2))

        tempResultArray = test1
        tempResultArrayString = bin(tempResultArray)

        originalArray = bin(self.bitArray)

        for i in range(self.filter_len):
            if tempResultArrayString[i+3] != originalArray[i+3]:
                return False
        return True