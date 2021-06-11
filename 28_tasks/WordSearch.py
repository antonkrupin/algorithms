def WordSearch(length, string, substring):
    splitString = []
    sequence = []
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
                if(n[-1] != ' '):
                    for i in reversed(range(len(m))):
                        if(m[i] == ' '):
                            splitString.append(m[:i])
                            pointer = pointer + i + 1
                            break
                        
            if(not ' ' in m):
                splitString.append(m)
                pointer = pointer + length    
    
    for x in range(len(splitString)):
        splitSubString = splitString[x].split()
        if(len(splitSubString) != 0):
            counter = 0
            for i in range(len(splitSubString)):
                if(substring == splitSubString[i]):
                    counter = counter + 1
            if(counter != 0):
                sequence.append(1)
            else:
                sequence.append(0)
    
    return sequence
