def WordSearch(l, string, subString):
    splitString = []
        
    stringLength = len(string)
    flag = True
    splitStart = 0
    
    x = string[splitStart:splitStart+l]
    
    if((len(x) == l) and (not ' ' in x)):
        splitString.append(x)
        splitStart = splitStart + l
    
    if(x[0] == ' '):
        x = string[splitStart+1:splitStart+l+1]
        if(' ' in x):
            #if(string[splitStart+l:splitStart+l+1] == ' '):
                #splitString.append(x)
                #splitStart = splitStart + l
            #else:
                for i in reversed(range(len(x))):
                    if(x[i] == ' '):
                        x = x[:i]
                        splitString.append(x)
                        splitStart = splitStart + i + 1
                        break
        else:
            splitString.append(x)
            splitStart = splitStart + l
    
    return splitString 