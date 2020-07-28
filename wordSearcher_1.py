def WordSearch(length, string, substring):
    splitString = []
    subStringLength = 0
    subs = ""
    string = string.strip().split()
    
    for x in range(len(string)):
        m = len(string[x])
        if(m > length):
            splitString.append(string[x][:length])
        if(m == length):
            splitString.append(string[x])
        if(m < length):
            j = x + 1
            test = []
            test.append(x)
            for j in range(len(string)):
                m = m + len(string[j])
                if(m == length):
                    test.append(j)
                    for i in range(len(test)):
                        splitString.append(string[test[i]] + ' ')
                if(m < length)
        
            
    
    return splitString
    
    
print(WordSearch(12," строка разбивается на набор строк через выравнивание по заданной ширине.", "строк"))
