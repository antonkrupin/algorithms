class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        #self.bitArray = [0] * self.filter_len
        self.bitArray = bin(2 ** self.filter_len)[3:]


    def hash1(self, str1):
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 17 + code) % 32
        return res
        # реализация ...

    def hash2(self, str1):
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 223 + code) % 32
        return res

    def add(self, str1):
        """
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        b1 = bin(h1)
        b2 = bin(h2)
        self.bitArray
        """
        pass

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        pass

