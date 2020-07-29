def WordSearch(length, string, substring):
    splitString = []
    
    pointer = 0
    
    if(length >= len(string)):
        splitString.append(string)
    else:
        while(pointer <= len(string)):
            m = string[pointer:pointer+length]
            n = string[pointer:pointer+length+1]
            if(' ' in m):
                if(n[-1] == ' '):
                    splitString.append(m)
                    pointer = pointer + length
                    #for i in reversed(range(len(m))):
                        #if(m[i] == ' '):
                            #splitString.append(m[:i])
                            #pointer = pointer + i + 1
                            #break
                if(n[-1] != ' '):
                    for i in reversed(range(len(m))):
                        if(m[i] == ' '):
                            splitString.append(m[:i])
                            pointer = pointer + i + 1
                            break
                        
            if(not ' ' in m):
                splitString.append(m)
                pointer = pointer + length    
    
    for x in range(len(splitString)-1):
        if(splitString[x] == ''):
            splitString.pop(x)
            
    print(splitString)
        
print(WordSearch(12,"строка разбивается на набор строк через выравнивание по заданной ширине.", "строк"))
