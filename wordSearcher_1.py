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
            splitString.append(string[x])
        
            
    
    return splitString
    
    
print(WordSearch(12," строка разбивается на набор строк через выравнивание по заданной ширине.", "строк"))